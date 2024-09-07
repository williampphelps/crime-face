<script>
    import { Card, Button, Label, Input, Checkbox } from 'flowbite-svelte';

    let error = '';
    let success = '';

    let signupData = {
        username: '',
        password: '',
        cpassword: '',
        rememberMe: false,
        type: 'Create'
    };

    const submitSignup = (e) => {
        e.preventDefault();
        if (signupData.password !== signupData.cpassword) {
            error = 'Passwords do not match!'
            success = '';
            return;
        } else {
          fetch('/login', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json'
              },
              body: JSON.stringify(signupData)
          }).then(res => { return res.json() })
              .then(data => {
                  if (data.error) {
                      error = data.error;
                      success = '';
                  } else {
                      error = '';
                      success = data.success;
                  }
              }).catch(err => {
                  console.log(err);
                  error = 'An error occurred. Please try again later.';
                  success = '';
          });
        }
        console.log(signupData);
    };

</script>
  

<div class="h-full w-full flex flex-col items-center justify-center">

    
      <Card>
        <form class="flex flex-col space-y-6" on:submit={submitSignup}>
          <h3 class="text-3xl font-bold text-gray-900 dark:text-white">Sign Up</h3>
          {#if error != ''}
          <p class="text-red-500">{error}</p>
          {/if}
          {#if success != ''}
          <p class="text-green-500">{success}</p>
          {/if}
          <Label class="space-y-2">
            <span>Username</span>
            <Input type="text" name="username" placeholder="name@company.com" bind:value={signupData.username} required />
          </Label>
          <Label class="space-y-2">
            <span>Your password</span>
            <Input type="password" name="password" placeholder="•••••" bind:value={signupData.password} required />
          </Label>
          <Label class="space-y-2">
            <span>Confirm password</span>
            <Input type="password" name="password" placeholder="•••••" bind:value={signupData.cpassword} required />
          </Label>
          <div class="flex items-start gap-1">
            <Checkbox bind:checked={signupData.rememberMe}>Agree with </Checkbox>
            <a href="/account/forgot" class="text-sm text-primary-700 hover:underline dark:text-primary-500">Privacy & Service Agreement </a>
          </div>
          <Button type="submit" class="w-full">Create Account</Button>
          <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
            Already registered? <a href="/account/login" class="text-primary-700 hover:underline dark:text-primary-500"> Log In </a>
          </div>
        </form>
      </Card>

</div>