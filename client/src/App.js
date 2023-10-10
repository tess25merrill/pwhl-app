import React from "react";
import { Switch, Route } from "react-router-dom";

import Header from "./components/Header";
import NavBar from "./components/NavBar";

function App() {


    return(
        <div>
            <Route exact path="/">
                <Header />
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
            </Route>
        </div>
    )
}

export default App