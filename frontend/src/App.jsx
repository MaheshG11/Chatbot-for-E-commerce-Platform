import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [value, setValue] = useState({
    productName: "",
    productID: "",
    category: "",
    brand: "",
    modelNumber: "",
    about: "",
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
      about: value.about,
      details: value.details,
      price: value.price,
      currency: value.currency,
      size: value.size,
      imgUrl: value.url,
    };
    // console.log(jsonData);
    try {
      const response = await axios.post("http://localhost:9000/", jsonData, {
        headers: {
          "Content-Type": "application/json",
        },
      });

      console.log("Form submitted successfully:", response.data);
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };
  return (
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
        <select
          name="category"
          id="category"
          onChange={(e) => handleChanges(e)}
        >
          <option value="" disabled selected hidden>
            Select Category
          </option>
          <option value="shirt">Shirt</option>
          <option value="tshirt">T-Shirt</option>
          <option value="jeans">Jeans</option>
          <option value="joggers">Joggers</option>
          <option value="jacket">Jacket</option>
          <option value="trousers">Trousers</option>
        </select>

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

        <label htmlFor="about">About</label>
        <textarea
          name="about"
          id="about"
          cols="30"
          rows="10"
          placeholder="Enter description"
          onChange={(e) => handleChanges(e)}
        ></textarea>

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

        <label htmlFor="size">Size</label>
        <select name="size" id="size" onChange={(e) => handleChanges(e)}>
          <option value="" disabled selected hidden>
            Select Size
          </option>
          <option value="S">S</option>
          <option value="M">M</option>
          <option value="L">L</option>
          <option value="XL">XL</option>
          <option value="XXL">XXL</option>
        </select>

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
  );
}

export default App;
