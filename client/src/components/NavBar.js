import React from "react";
import { NavLink } from "react-router-dom";

function NavBar() {


    return (
        <table>
            <tr>
                <button class="navbar">Home</button>
            </tr>
            <tr>
                <button class="navbar">Quizzes</button>
            </tr>
            <tr>
                <button class="navbar">Leaderboard</button>
            </tr>
            <tr>
                <button class="navbar">News</button>
            </tr>
            <tr>
                <button class="navbar">Get Involved</button>
            </tr>
            <tr>
                <button class="navbar">My Account</button>
            </tr>
        </table>
    )
}

export default NavBar