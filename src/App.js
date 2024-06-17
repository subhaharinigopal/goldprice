import React from "react"
import LandingPage from "./Components/LandingPage"
import Content from "./Components/Content"
import Result from './Components/Result';
import { BrowserRouter , Route, Routes } from "react-router-dom"


const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/content" element={<Content/>} />
        <Route path="/result" element={<Result/>} />
        <Route path="*" element={<h1>404 Not Found</h1>} />
      </Routes>
    </BrowserRouter>


  )
}

export default App