document.addEventListener("DOMContentLoaded", function() {

    const btnEnviar = document.getElementById("btnEnviar");
    const inputEntrada = document.getElementById("entrada");
  
    const EnviarMensaje = () => {
        let entrada = inputEntrada.value;
      
        // Crea un objeto FormData y agrega el valor de entrada al formulario
        const formData = new FormData();
        formData.append('entrada', entrada);
      
        // Realiza la solicitud POST con el formulario como datos
        axios.post('/chatbot', formData)
          .then(function(response) {
            const respuesta = response.data;
            console.log(respuesta);
          })
          .catch(function(error) {
            console.error(error);
          });
      }
  
    btnEnviar.addEventListener("click", EnviarMensaje);

  });
  
  
  
  
  
  
  