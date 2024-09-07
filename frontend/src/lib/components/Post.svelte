<script>

    import { Card, Label, Input, Button, Badge } from 'flowbite-svelte';
    import { ThumbsUpOutline, ThumbsDownOutline, ClockOutline, UserOutline } from 'flowbite-svelte-icons';
    import { onMount } from 'svelte';
    import Time from 'svelte-time';

    let showDecrypt = false;
    let decryptPassword = '';
    let error = '';

    const toggleDecrypt = () => {
        showDecrypt = !showDecrypt;
    }

    const addLike = () => {
        // Send a request to the server with the post id to add a like
    }
    const removeLike = () => {
        // Send a request to the server with the post id to remove a like
    }

    export let post;

    const standardizeTime = (time) => {
        return new Date(time * 1000).toISOString();
    }

    const decryptPost = () => {
        // Send a request to the server with the post id and the password and update the post text with the decrypted text
        fetch('/api/posts/decrypt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: post.id,
                password: decryptPassword
            })
        }).then(res => {
            return res.json();
        }).then(data => {
            if (data.error) {
                error = data.error;
                return;
            }
            post.text = data.content;
            error = '';
        }).catch(err => {
            console.log(err);
        });
    }
</script>
<Card class="w-full" size="lg">
    <p class="font-normal text-gray-700 dark:text-gray-400 leading-tight mb-4">{post.text}</p>
    <div class="flex flex-row gap-4">
        <Badge color='dark'><span class="flex flex-row gap-2 items-center"><UserOutline /> {post.user}</span></Badge>
        <Badge color='dark'><span class="flex flex-row gap-2 items-center"><ClockOutline /> <Time timestamp={standardizeTime(post.time)} relative /></span></Badge>
        <span>
            <Badge color="green" class="cursor-pointer" on:click={addLike}><ThumbsUpOutline /> 3</Badge>
            <Badge color="red" class="cursor-pointer" on:click={removeLike}><ThumbsDownOutline /> 3</Badge>
        </span>
    </div>
    
    <form on:submit|preventDefault={decryptPost} class="flex flex-row gap-2 mt-5 w-full">
        <div class='flex flex-col gap-2'>
            <Input size="sm" type="password" placeholder="Decryption Password" bind:value={decryptPassword} />
            {#if error != ''}
                <small class="text-red-500">{error}</small>
            {/if}
        </div>
        <Button type="submit" size="xs" color="primary">Decrypt</Button>
    </form>
</Card>