$(document).ready(function() {
    showData();
    $(".btn .btn-link .purchasebutton").click(function(){
            alert("El articulo fue agregado a su lista de favoritos");
    });

    $(".btn .btn-primary").on("click", function(){
        alert("Plataforma de compra");
    });
})



function getData(){
    return new Promise((resolve, reject) => {
        $.getJSON(
            "http://localhost:3000/orders/getproducts?format=json",
            (data) => {
                if(data){
                    resolve(data);
                } else {
                    reject("Error al obtener los datos");
                }
            },

        );
    });
}


function getCategories(){
    return new Promise((resolve, reject) => {
        $.getJSON(
            "http://localhost:3000/orders/getcategories?format=json",
            (data) => {
                if(data){
                    resolve(data);
                } else {
                    reject("Error al obtener los datos");
                }
            },
        );
    });

}

function showCategories(category){
    return `
            <button class="dropdown-item" href="#">${category.category_name}</button>
        `

}
    

function createCard(product){
    
    return `
    <div class="col-sm-6 col-md-4 col-lg-3 d-flex align-items-stretch">
        <div class="card mb-4">
        <div class="embed-responsive embed-responsive-16by9">
            <img src="${product.image_url}" class="card-img-top img-responsive" alt="Imagen de la tarjeta">
                <div class="card-body">
                    <h6 class="card-subtitle mb-2 text-muted"> 
                        ${product.item_subcategory.subcategory_name}
                    </h6>
                    <h5 class="card-title fw-bold">
                        ${product.name}
                    </h5>
                    <p class="card-text">
                       $${product.item_price}
                    </p>
                    <a class="btn btn-primary purchasebutton" data-mdb-color="purple">Comprar</a>
                    <a class="btn btn-link favbutton"><i class="fa fa-heart"></i> Agregar a favoritos</i></a>
                </div>
             </div>
        </div>
    </div>
    `
}

function register(){
    $("#loginProfile").change(function(){
        window.Location.href="/frontend/login.html";
    });
}

async function showData(){

    try{
        const datacards = await getData();
        const datacat= await getCategories();
        let cards= "";
        let cats="";

        datacards.forEach(product=> {
            cards+=createCard(product);
        });

        datacat.forEach(category=>{
            cats+=showCategories(category);
        });

        $("#cardContainer").html(cards);
        $("#categoriesDropdown").html(cats);

    } catch(error){
        console.error(error);
    }

}