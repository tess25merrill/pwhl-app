import React, {useEffect, useState} from "react";
import { Switch, Route } from "react-router-dom";

import Header from "./components/Header";
import NavBar from "./components/NavBar";
import Login from "./components/Login";

const baseUrl = "http://127.0.0.1:5555"
const chkSessionUrl = baseUrl + "/check-session"

function App() {

const [user, setUser] = useState(null);

useEffect(() => {
    fetch(chkSessionUrl)
    .then(r => {
        if (r.ok) {
        r.json().then((user) => setUser(user))
        }
    })
    }, [])

    function handleUserSet(user) {
        setUser(user);
        console.log(`User set to ${user.name}`);
    }
    
    function handleLogout() {
        setUser(null);
    }

    return(
        <div>
            <Header />
            <NavBar />
            <Login />
            {/* <Route exact path="/"> */}
                {/* <Login handleUserSet={handleUserSet}/>
            </Route>
            <Route exact path="/home">
                <NavBar />
            </Route>
            <Route exact path="/quizzes">
                <NavBar />
            </Route>
            <Route exact path="/leaderboard">
                <NavBar />
            </Route>
            <Route exact path="/news">
                <NavBar />
            </Route>
            <Route exact path="/involvement">
                <NavBar />
            </Route>
            <Route exact path="/account">
                <NavBar />
            </Route> */}
        </div>
    )
}

export default App