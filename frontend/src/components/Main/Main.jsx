import React, { useState,useEffect } from "react";
import "./Main.css";
import { assets } from "../../assets/assets";
import axios from "axios";
import myObject from '../../env';
import { Link,useNavigate} from 'react-router-dom';
import ProductCard from "./productcard"
const Main = () => {
  const [prompt,setPrompt]=useState("");
  const [url,setUrl]=useState("");
  const [extended, setextended] = useState(0);
  const [response, setResponse] = useState(''); // State variable for the response
  const [isLoading, setIsLoading] = useState(false); // State variable for loading state
  const [messages, setMessages] = useState([ ]);

  const handleClick= async (e)=>{
    e.preventDefault();
    const jsonData={
      query: prompt,
    };
    console.log(prompt)
    
    setIsLoading(true); 
    try {
      const res=await axios.post(`${myObject.BASE_URL}/infer`,jsonData,{
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (res.status === 200) { 
        setMessages([...messages, { type: 'user', text: prompt,products:[] }, { type: 'bot', text: res.data['response'],products:res.data['products']}]);
        if(res.data['products'])
        setResponse(res.data.response); 
        console.log(res)
        setPrompt(''); 
      } else {
        console.error('Error:', res.status); 
      }
    } catch (error) {

      console.error('Error:', error); 
    } finally {
      setIsLoading(false); 
    }
    
  }
  const handleChange=(e)=>{
    setPrompt(e.target.value);
    // setPrompt();
    
  }
   // Re-render the previous prompt if response is not received
  //  useEffect(() => {
  //   if (isLoading && !response) {
  //     setPrompt(prompt);
  //   }
  //   else {
  //     setPrompt('')
  //   }
  // }, [isLoading, response]);

  const navigate = useNavigate();
  return (
    <div className="main">
      <div className="nav">
        <p>Gemini</p>
        <button  onClick={() => navigate('/upload_products')}>Upload Product Here</button>
        <img src={assets.user_icon} alt="" />
      </div>
      <div className="main-container">
        

        <div className="chat-container">
        
      {messages.map((message, index) => (
  <div key={index} className={`message ${message.type}`}>
    {message.text}
    <br /> 
    {message.products && message.products.length > 0 && ( // Check within the message object
      <div className="product-container cards">
        {message.products.map((product, productIndex) => (
          <ProductCard product={product} key={productIndex} /> // Use appropriate component name
        ))}
      </div>
    )}
  </div>
))}
      </div>
      <div className="main-bottom">
        
          <div className="search-box">
            <input 
            onChange={handleChange} 
            type="text" 
            placeholder="Enter a prompt here" 
            value={prompt} // Set input value to reflect the prompt
            disabled={isLoading} // Disable input while loading
            />
            <div>
              <img src={assets.send_icon} alt="" onClick={handleClick}/>
            </div>
          </div>
          <p className="bottom-info">
            E-commerce Chat Agent may display inaccuarte info.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Main;
