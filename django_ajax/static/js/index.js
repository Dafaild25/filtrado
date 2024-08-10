const listarPaises=async()=>{
    try {
        const response=await fetch("./listarPaises");
        const data = await response.json();
        console.log(data)
        if(data.message==="Se Logro"){
            let opciones = ``;
            data.paises.forEach((pais)=>{
                opciones+=`<option value='${pais.id}'>${pais.nombre}</option>`;
            });
            cboPais.innerHTML=opciones  ;
            listarCiudades(data.paises[0].id);
        }
        else{
            alert("Paises no encontrados")
        }
    } catch (error) {
        console.log(error);
        
    }
}

const listarCiudades = async(idPais)=>{
    try {
        const response = await fetch(`./listarCiudades/${idPais}/`);
        //const response = await fetch('./listarCiudades/1');
        const data =  await response.json();
        if (data.message=="Se logro"){
            let opciones = ``;
            data.ciudades.forEach((ciudades)=>{
                opciones+=`<option value= '${ciudades.id}'>${ciudades.nombre}</option>`;
            })
            cboCiudades.innerHTML=opciones;
        }
        else{
            console.log("No se encontraron datos ")
        }    
    } catch (error) {
        console.log(error)
    }
}
const cargaInicial = async()=>{
    await listarPaises();
    cboPais.addEventListener("change",(event)=>{
        console.log(event)
        console.log(event.target)
        console.log(event.target.value)
        var dato = event.target.value
        listarCiudades(dato);
    })
    
}


window.addEventListener("load",async()=>{
    await cargaInicial()
})