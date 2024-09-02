import './productcard.css'

import React from 'react';


function ProductCard({product,index}) {
  return (
    // <div className="cards">
          
          <div className="card product-card" href={product.link}>
            <a href={product.link} className="product-card-link"> 
          <img key={index} src={product.imgUrl} alt={`Image Not found`} />
          <p className="product-name">{product.name}</p>
       <p className="product-price">Price: {product.price}</p> {/* Format price to 2 decimal places */}
      </a>
          </div>
          
        
  );
}

export default ProductCard;