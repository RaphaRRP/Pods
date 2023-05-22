Swal.fire({
  width: 300,
  imageUrl: 'https://images.emojiterra.com/mozilla/512px/1f51e.png',
  title: 'Site destinado á pessoas que querem parar de fumar',
  text: 'Você possue 18 anos ou mais?',
  
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Sim',
  showDenyButton: true,
  denyButtonText: 'Não',
})
.then((result) => {
  if (result.isConfirmed) {
  }
  else{
    window.close()
  }
})


// Array para armazenar os produtos selecionados
var cartItems = [];


// Função para adicionar um item ao carrinho
function addToCart(item) {
  cartItems.push(item);
  updateCart();
}

// Função para atualizar o carrinho
function updateCart() {
  var cartList = document.getElementById("cart-items");
  var cartTotal = document.getElementById("cart-total");
  cartList.innerHTML = "";
  var total = 0;
  for (var i = 0; i < cartItems.length; i++) {
    var li = document.createElement("li");
    li.innerText = cartItems[i];
    cartList.appendChild(li);
    total += parseFloat(cartItems[i].split("R$")[1]);
  }
  cartTotal.innerText = "Total: R$" + total.toFixed(2);
}

// Função para finalizar a compra
function checkout() {
  alert("Compra finalizada! Total: R$" + parseFloat(document.getElementById("cart-total").innerText.split("R$")[1]).toFixed(2));

  cartItems = [];
  updateCart();
}

// Função para limpar o carrinho
function clearCart() {
  cartItems = [];
  updateCart();
}

// Chamando a função de atualização do carrinho inicialmente
updateCart();