import React,{ useState } from 'react'
import Sidebar from './components/Sidebar/Sidebar'
import Main from './components/Main/Main'
import ProductDetails from './components/ProductDetails/ProductDetails'
import { assets } from './assets/assets'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import "./App.css"
import { Link,useNavigate} from 'react-router-dom';
import Routing from './components/Routing'
const App = () => {
  
  const [changePage, setchangePage] = useState(1);

  return (
    <>
     
     <Router>
     <Sidebar/>
<Routes>

  <Route path="/" element={<Routing/>}/>
  <Route path="/upload_products" element={<ProductDetails/>} />
  <Route path="/chat" element={<Main/>} />
</Routes>
</Router>
    
    
    </>
  )
}

export default App