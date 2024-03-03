let quantity = 1;

    function increment() {
        quantity++;
        document.getElementById('quantity').innerText = quantity;
    }

    function decrement() {
        if (quantity > 1) {
            quantity--;
            document.getElementById('quantity').innerText = quantity;
        }
    }