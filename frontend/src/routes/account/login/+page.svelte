<script>
    import { Card, Button, Label, Input, Checkbox } from 'flowbite-svelte';

    let loginData = {
        username: '',
        password: '',
        type: 'Login'
    };

    let error = '';
    let success = '';

    const submitLogin = (e) => {
        e.preventDefault();
        console.log(loginData);
        // post to /login with loginData
        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(loginData)
        }).then(res => { return res.json() })
              .then(data => {
                  if (data.error) {
                      error = data.error;
                      success = '';
                  } else {
                      error = '';
                      success = data.success;
                      window.location.href = '/';
                  }
              }).catch(err => {
                  console.log(err);
                  error = 'An error occurred. Please try again later.';
                  success = '';
          });
    };

</script>
  

<div class="h-full w-full flex flex-col items-center justify-center">

    
      <Card>
        <form class="flex flex-col space-y-6" on:submit={submitLogin}>
          <h3 class="text-3xl font-bold text-gray-900 dark:text-white">Sign In</h3>
          {#if error != ''}
          <p class="text-red-500">{error}</p>
          {/if}
          {#if success != ''}
          <p class="text-green-500">{success}</p>
          {/if}
          <Label class="space-y-2">
            <span>Username</span>
            <Input type="text" name="username" placeholder="name@company.com" bind:value={loginData.username} required />
          </Label>
          <Label class="space-y-2">
            <span>Your password</span>
            <Input type="password" name="password" placeholder="•••••" bind:value={loginData.password} required />
          </Label>
          <div class="flex items-start">
            <Checkbox bind:checked={loginData.rememberMe}>Remember me</Checkbox>
            <a href="/account/forgot" class="ms-auto text-sm text-primary-700 hover:underline dark:text-primary-500"> Lost password? </a>
          </div>
          <Button type="submit" class="w-full">Login to your account</Button>
          <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
            Not registered? <a href="/account/signup" class="text-primary-700 hover:underline dark:text-primary-500"> Create account </a>
          </div>
        </form>
      </Card>

</div>