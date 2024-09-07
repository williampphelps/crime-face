<script>
import "../app.pcss";

import {browser} from '$app/environment';

import { Navbar, NavBrand, NavHamburger, NavUl, NavLi, DarkMode, Button } from "flowbite-svelte";

let loggedIn = false;

// check for cookies 'username' and 'password'
if (browser) {
    if (document.cookie.includes('username') && document.cookie.includes('password')) {
        loggedIn = true;
    }
}

const logout = () => {
    // send POST request to /logout
    fetch('/logout', {
        method: 'POST'
    }).then(res => {
        if (res.ok) {
            loggedIn = false;
            // refresh the page
            location.reload();
        }
    });
}


</script>
<div class="md:h-screen h-fit w-screen px-8">
    <Navbar class="px-12 py-2.5 fixed w-full z-20 top-0 start-0 border-b">
        <NavBrand href="/">
            <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Crime Face</span>
        </NavBrand>
        <div class="flex md:order-2">
            {#if loggedIn}
            <Button on:click={logout} size='sm'>Logout</Button>
            {/if}
            <NavHamburger />
          </div>
        <NavUl class='ml-auto'>
            <NavLi href="/">Home</NavLi>
            {#if !loggedIn}
            <NavLi href="/account/login">Login</NavLi>
            <NavLi href="/account/signup">Sign Up</NavLi>
            {/if}
        </NavUl>
        <NavUl>
            <DarkMode />
        </NavUl>
    </Navbar>
    <div class="h-full overflow-auto w-full pt-24">
        <slot />
    </div>

</div>
