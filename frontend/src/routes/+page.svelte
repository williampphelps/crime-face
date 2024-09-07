<script>

    import {Card, Button, Input, Textarea, Label, Listgroup, ListgroupItem} from 'flowbite-svelte';

    import Post from '$lib/components/Post.svelte';
    import { onMount } from 'svelte';
    import { browser } from '$app/environment';
    import { get } from 'svelte/store';

    let addFriendUsername = '';

    let currentUser = {
        username: ''
    }

    let newPost = {
        content: '',
        password: ''
    }

    const addFriend = (e) => {
        // Send a post request to /addfriend with the username
        e.preventDefault();
        fetch('/addfriend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({username: addFriendUsername})
        }).then(res => {
            if (res.ok) {
                // Add the friend to the friendsList
                friendsList = [...friendsList, addFriendUsername];
                addFriendUsername = '';
            }


            getPosts();
            getCurrentUser();
        });

    }

    let posts = [];
    let friendsList = [];
    // let currentUser;

    const getPosts = async () => {
        const res = await fetch('/api/posts');
        const data = await res.json();
        posts = data.posts;
    }

    const createPost = async (e) => {
        e.preventDefault();
        const res = await fetch('/api/posts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newPost)
        });
        const data = await res.json();
        getPosts();
        newPost = {
            content: '',
            password: ''
        }
    }

    const getCurrentUser = async () => {
        if (browser) {
            if (document.cookie.includes('username') && document.cookie.includes('password')) {
                currentUser = {
                    username: document.cookie.split('; ').find(row => row.startsWith('username')).split('=')[1]
                }


                const res = await fetch('/api/user/' + currentUser.username);
                const data = await res.json();
                friendsList = data.friends;
            }
        }
    }

    onMount(() => {
        getPosts();
        getCurrentUser();
    });
</script>
<div class="p-4 flex lg:flex-row flex-col lg:justify-between justify-evenly gap-4 w-full h-full overflow-auto">
    <div class="flex flex-col w-full lg:w-fit items-center grow-0">
        <Card class='w-full h-fit' size='lg'>
            <h3 class="text-3xl font-bold text-gray-900 dark:text-white">New Post</h3>
            <form on:submit|preventDefault={createPost}>
                <div class="flex flex-col gap-4 pt-8">
                    <span class="flex flex-col gap-2">
                        <Label>Create Post</Label>
                        <Textarea name="content" placeholder="Post content" bind:value={newPost.content} required />
                    </span>
                    <span class="flex flex-col gap-2">
                        <Label>Password (leave blank for no encryption)</Label>
                        <Input name="password" type="password" placeholder="Password" bind:value={newPost.password} />
                    </span>
                    
                    <Button type="submit" class="w-full">Create Post</Button>
                </div>
            </form>
        </Card>
    </div>
    <div class="flex flex-col items-center gap-4 lg:overflow-auto grow">
        {#if posts.length == 0}
            <h3 class="text-3xl font-bold text-gray-900 dark:text-white">No Posts Yet</h3>
        {/if}
        {#each posts as post}
            <Post {post} />
        {/each}
    </div>
    <div class="flex flex-col gap-4 items-center grow-0">
        <Card class="flex flex-col gap-4 w-full" size='lg'>
            <h3 class="font-bold">Add Friends</h3>
            <form class="flex flex-col gap-4" on:submit|preventDefault={addFriend}>
                <Input type="text" name="friend" placeholder="Enter Friend's Username Here..." bind:value={addFriendUsername} required />
                <Button type="submit">Add Friend</Button>
            </form>
        </Card>

        <Listgroup class="self-stretch">
            <h3 class="p-3 font-bold">Friends List</h3>
            {#each friendsList as friend}
                <ListgroupItem>{friend}</ListgroupItem>
            {/each}
        </Listgroup>
    </div>
</div>