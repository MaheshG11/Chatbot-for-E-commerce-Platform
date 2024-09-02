import { useState } from "react";
import axios from "axios";
import "./ProductDetails.css";
import { Link,useNavigate} from 'react-router-dom';
function ProductDetails() {
  const [value, setValue] = useState({
    productName: "",
    productID: "",
    category: "",
    brand: "",
    modelNumber: "",
    details: "",
    price: "",
    currency: "",
    size: "",
    imgUrl: "",
  });

  const handleChanges = (e) => {
    console.log(e);
    setValue({ ...value, [e.target.name]: [e.target.value] });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const jsonData = {
      productName: value.productName,
      productID: value.productID,
      category: value.category,
      brand: value.brand,
      modelNumber: value.modelNumber,
      details: value.details,
      price: value.price,
      currency: value.currency,
      size: value.size,
      imgUrl: value.imgUrl,
    };
    // console.log(jsonData);
    try {
      const response = await axios.post("http://localhost:8002/ingest", jsonData, {
        headers: {
          "Content-Type": "application/json",
        },
      });

      console.log("Form submitted successfully:", response.data);
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };
  const navigate = useNavigate();
  return (
    <div className="cen">  
    <div className="nav">
    <p>Gemini</p>
    <button style={{  backgroundColor: '#585858'} } onClick={() => navigate('/chat') }>Chat Here</button>
  </div>
    <div className="container">
   
      <h1>Product Details</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="productName">Product Name</label>
        <input
          type="text"
          placeholder="Enter the Product Name"
          name="productName"
          onChange={(e) => handleChanges(e)}
        />

        <label htmlFor="productID">Product ID/SKU</label>
        <input
          type="text"
          placeholder="Enter the Product ID/SKU"
          name="productID"
          onChange={(e) => handleChanges(e)}
        />


        <label htmlFor="category">Category</label>
        <input
          type="text"
          placeholder="Enter the Category of the product"
          name="category"
          onChange={(e) => handleChanges(e)}
        />
        <label htmlFor="brand">Brand</label>
        <input
          type="text"
          placeholder="Enter the Brand"
          name="brand"
          onChange={(e) => handleChanges(e)}
        />

        <label htmlFor="modelNumber">Model Number</label>
        <input
          type="text"
          placeholder="Enter the Model Number"
          name="modelNumber"
          onChange={(e) => handleChanges(e)}
        />

 
        <label htmlFor="details">Details</label>
        <textarea
          name="details"
          id="details"
          cols="30"
          rows="10"
          placeholder="Enter Details"
          onChange={(e) => handleChanges(e)}
        ></textarea>

        <label htmlFor="price">Price</label>
        <input
          type="number"
          placeholder="Enter the Price"
          name="price"
          onChange={(e) => handleChanges(e)}
        />

        <label htmlFor="currency">Currency</label>
        <select
          name="currency"
          id="currency"
          onChange={(e) => handleChanges(e)}
        >
          <option value="" disabled selected hidden>
            Select Currency
          </option>
          <option value="USD">&#36; - USD</option>
          <option value="INR">&#8377; - INR</option>
          <option value="Ruble">&#8381; - Ruble</option>
          <option value="Yen">&#165; - Yen</option>
        </select>

        <label htmlFor="size">size</label>
        <input
          type="text"
          placeholder="Enter size of product"
          name="size"
          onChange={(e) => handleChanges(e)}
        />

        {/* <label htmlFor='image'>Select Image</label>
        <input type='file' name='image' accept='image/*' placeholder='Select the file' 
        onChange={(e) => handleChanges(e)}/>

        <label for="frontView">Front View:</label>
        <input type="file" id="frontView" name="frontView" accept="image/*" 
        onChange={(e) => handleChanges(e)}/>
    
        <label for="sideView">Side View:</label>
        <input type="file" id="sideView" name="sideView" accept="image/*" 
        onChange={(e) => handleChanges(e)}/>

        <label for="packaging">Packaging:</label>
        <input type="file" id="packaging" name="packaging" accept="image/*" 
        onChange={(e) => handleChanges(e)}/> */}
        <label htmlFor="imgUrl">Image URL</label>
        <input
          type="text"
          placeholder="Enter the Image url"
          name="imgUrl"
          onChange={(e) => handleChanges(e)}
        />
        {/* <label htmlFor='url'>Video URL</label>
        <input type='text' placeholder='Enter the Video url' name='url'
        onChange={(e) => handleChanges(e)}/> */}

        <button type="submit">submit</button>
      </form>
    </div>
    </div>
  );
}

export default ProductDetails;
