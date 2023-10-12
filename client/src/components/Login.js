import React, {useState} from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";

const baseUrl = 'http://127.0.0.1:5555'
const loginUrl = baseUrl + '/login'
const createAcctUrl = baseUrl + '/create-account'

function Login({handleUserSet}) {

    const [loginClick, setLoginClick] = useState(false)
    const [createAcctClick, setCreateAcctClick] = useState(false)

    const [email, setEmail] = useState("")
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const history = useHistory()

    function handleLogin(e) {
        e.preventDefault()
        fetch(loginUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            }, body: JSON.stringify({email, password})
        })
        .then(r => {
            if (r.ok) {
                r.json().then(user => handleUserSet(user))
                setUsername("")
                setPassword("")
                history.push('/')
            } else {
                console.log("User not logged in")
            }
        })
    }

    function handleCreateAcct(e) {
        e.preventDefault()
        fetch(createAcctUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            }, body: JSON.stringify({username, email, password})
        })
        .then(r => {
            if (r.ok) {
                r.json().then(user => handleUserSet(user))
                setUsername("")
                setEmail("")
                setPassword("")
                history.push('/')
            } else {
                console.log("User not created")
            }
        })
    }
    

    return (
        <div>
            <p>Get to know the PWHL! Learn all about the teams and players to watch before the inaugural season.</p>
            <div>
                {loginClick ?
                <form onSubmit={handleLogin}>
                    <input 
                        type="text" 
                        placeholder="username" 
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)}>
                    </input>
                    <input 
                        type="password" 
                        placeholder="password" 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)}>
                    </input>
                    <button type="submit">Login</button>
                </form>
                : <button onClick={() => setLoginClick(!loginClick)}>Log In</button>
            }
            {createAcctClick ?
                <form onSubmit={handleCreateAcct}>
                    <input 
                        type="text" 
                        placeholder="username" 
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)}>
                    </input>
                    <input 
                        type="text" 
                        placeholder="email" 
                        value={email} 
                        onChange={(e) => setEmail(e.target.value)}>
                    </input>
                    <input 
                        type="text" 
                        placeholder="password" 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)}>
                    </input>
                    <button type="submit">Create Account</button>
                </form>
                : <button onClick={() => setCreateAcctClick(!createAcctClick)}>Create Account</button>
            }
            </div>
        </div>
        )
}


export default Login