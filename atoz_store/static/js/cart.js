var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i<updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    var flagg =this.dataset.flagu

    
 
    console.log('productId:',productId,'action:',action)
    console.log('USER:',user)
    if(user === 'AnonymousUser'){
        addCookieItem(productId,action,flagg)

    }
    else{
        updateUserOrder(productId,action)
           
        }
    

    })
}

function addCookieItem(productId,action,flag){
  
    if(action == 'add')
    {
        if(cart[productId] == undefined)
        {
            console.log('werehere')
            cart[productId] = {'quantity':1}
        
        }
        else
        {
            if(flag){
                cart[productId]['quantity'] +=1
            }
           
            else{
                cart[productId]['quantity'] +=0.250
            }
                   
    }
}
    if(action == 'remove'){
        if(flag){
        cart[productId]['quantity'] -=1
        }
        else{
        cart[productId]['quantity'] -=0.250
        }
        if(cart[productId]['quantity']<=0.000){
            console.log("remove item")
            delete cart[productId]
        }

        
    }
    console.log('cart:',cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;PATH=/'
    location.reload()
}

function updateUserOrder(productId,action){
    if(action==undefined)
    {
        action="add"
    }
    console.log(productId,action)
    console.log('user is logged in, sending data')  

    var url = '/updateItem/'
    fetch(url, {
        method :'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId,'action':action})
    })
    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
    
    
    

    }
var cart_icon = document.getElementById("cart-total")
function cartIcon(noOfitems){
    //no of items in cart

}