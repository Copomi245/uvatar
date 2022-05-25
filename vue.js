//JavaScript que no tengo muy claro que hace
//El vue
const app = new Vue({
    el: '#app',
    data: {
        cara:{},
        orejaIzquierda:[],
        orejaDerecha:{},
        ojos:{},
        boca:{},
        nariz:{}

    },
    created(){
                
    }, 
    methods:{
        uvatarAleatorio(){
            const vm = this
            fetch('http://localhost:8080/Aleatorio')
            .then(response => response.json())
            .then(json => {
                vm.orejaIzquierda = json.orejaI.url
                vm.orejaDerecha = json.orejaD.url
                vm.ojos = json.ojos.url
                vm.boca = json.boca.url    
                vm.nariz = json.nariz.url
                
                
                
        })
        },
        cambiarCara(cara){},
        cambiarOjos(ojos){},
        cambiarBoca(boca){},
        cambiarOrejaI(oreja){},
        cambiarOrejaD(oreja){}
    }
})

