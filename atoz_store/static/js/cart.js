var updateBtns = document.getElementsByClassName('update-cart')
var setstatus = document.getElementsByClassName('setstatus')
var cartBtns = document.getElementsByClassName('cart-button')
        
    

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
    console.log(flag)

    if(action == 'add')
    {
        if(cart[productId] ==undefined)
        {
            console.log('werehere')
            cart[productId] = {'quantity':1}
        
        }
        else
        {
            if(flag==='True'){
                console.log("+1",flag)
              cart[productId]['quantity'] += 0.250
            }
           
            else{

                console.log("0.25",flag)
            cart[productId]['quantity'] += 1.000
            }
                   
    }
}
    if(action == 'remove'){
        if(flag==="True"){
        cart[productId]['quantity'] -= 0.250
        }
        else{
        cart[productId]['quantity'] -= 1.000
        }
        if(cart[productId]['quantity']<=0.000){
            console.log("remove item")
            delete cart[productId]
        }

        
    }

    if(action == 'delete'){
        delete cart[productId]
    }

    console.log('cart:',cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;PATH=/'
    location.reload()
}

function updateUserOrder(productId,action){

  
    
    
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
   
    
    //store add to cart buttons
    for(var i=0; i<cartBtns.length;i++){
        cartBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var flagg =this.dataset.flagu
        
     
        console.log('productId:',productId,'action:',action)
        console.log('USER:',user)
        if(user === 'AnonymousUser'){
            addCookieItem1(productId,action,flagg)
    
        }
        else{
            
            updateUserOrder1(productId,action)
               
            }
        
    
        })
    }
    
    function addCookieItem1(productId,action,flag){
        console.log(flag)
    
        if(action == 'add')
        {
            if(cart[productId] ==undefined)
            {
                console.log('werehere')
                cart[productId] = {'quantity':1}
            
            }
            else
            {
                if(flag==='True'){
                    console.log("+1",flag)
                  cart[productId]['quantity'] += 0.250
                }
               
                else{
    
                    console.log("0.25",flag)
                cart[productId]['quantity'] += 1.000
                }
                       
        }
    }
        if(action == 'remove'){
            if(flag==="True"){
            cart[productId]['quantity'] -= 0.250
            }
            else{
            cart[productId]['quantity'] -= 1.000
            }
            if(cart[productId]['quantity']<=0.000){
                console.log("remove item")
                delete cart[productId]
            }
    
            
        }
    
        if(action == 'delete'){
            delete cart[productId]
        }
    
        console.log('cart:',cart)
        document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;PATH=/'
        $( "#number" ).load(window.location.href + " #number" );
        $( "#cart-total1" ).load(window.location.href + " #cart-total1" );
        
    }

    function updateUserOrder1(productId,action){
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
        
        })
        $( "#number" ).load(window.location.href + " #number" );
        $( "#cart-total1" ).load(window.location.href + " #cart-total1" );
        
        
    
        }
       
//end store buttons    