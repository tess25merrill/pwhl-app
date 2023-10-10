const routes = [
    {
    path: "/",
    element: <Home />,
    errorElement: <ErrorPage />
    }, 
    {
    path: "/quizzes",
    element: <Quiz />,
    errorElement: <ErrorPage />
    },
    {
    path: "/leaderboard",
    element: <Login />,
    errorElement: <ErrorPage />
    },
    {
    path: "/news",
    element: <UserProfile />,
    errorElement: <ErrorPage />
    },
    {
    path: "/involvement",
    element: <UserProfile />,
    errorElement: <ErrorPage />
    }
];