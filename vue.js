//JavaScript que no tengo muy claro que hace
//El vue
const app = new Vue({
    el: '#app',
    data: {
        nombre:null,
        ojos_actual:[],
        nariz_actual:[],
        orejaI_actual:[],
        orejaD_actual:[],
        boca_actual:[],
        accesorio_cabeza:[],
        accesorio_facial:[],
        pelo:[],
        cara:"carne con salsa",
        ojos:[],
        bocas:[],
        narices:[],
        orejasI:["cagon"],
        orejasD:[],
        accesorios:[],
        variable:[],

    },
    created(){


module.exports = {
  runtimeCompiler: true
}
        
        fetch('http://::8080/ojos')
        .then(response => response.json())
        .then(json => {
            this.ojos = json.Ojos
        }),

        fetch('http://::8080/bocas')
        .then(response => response.json())
        .then(json => {
            this.bocas = json.Bocas
        }),

        fetch('http://::8080/narices')
        .then(response => response.json())
        .then(json => {
            this.narices = json.Narices
        }),

        fetch('http://::8080/orejasI')
        .then(response => response.json())
        .then(json => {
            this.orejasI = json.Orejas
        }),

        fetch('http://::8080/orejasD')
        .then(response => response.json())
        .then(json => {
            this.orejasD = json.Orejas
        }),

        fetch('http://::8080/accesorios')
        .then(response => response.json())
        .then(json => {
            this.accesorios = json.Accesorios
        })


        


                
    }, 
    methods:{
        uvatarAleatorio(){
 
            this.orejaD_actual.push(orejasD[Math.floor(Math.random()*orejasD.length)])
            this.orejaI_actual.push(orejasI[Math.floor(Math.random()*orejasI.length)])
            this.boca_actual.push(bocas[Math.floor(Math.random()*bocas.length)])
            this.nariz_actual.push(narices[Math.floor(Math.random()*narices.length)])
            this.ojos_actual.push(ojos[Math.floor(Math.random()*ojos.length)])
        },
        
        cambiarOjos(ojo){
            this.ojos_actual = []
            this.ojos_actual.push(ojo)
        },

        cambiarBoca(boca){
            this.boca_actual = []
            this.boca_actual.push(boca)
        },
        cambiarOrejaI(oreja){
            this.orejaI_actual = []
            this.orejaI_actual.push(oreja)
        },
        cambiarOrejaD(oreja){
            this.orejaD_actual = []
            this.orejaD_actual.push(oreja)
        },
        cambiarNariz(nariz){
            this.nariz_actual = []
            this.nariz_actual.push(nariz)
        },
        equiparAccesorio(accesorio){
            this.accesorio_cabeza = []
            this.accesorio_cabeza.push(accesorio)


        },

        random(){
            this.ojos_actual = []
            this.ojos_actual=this.ojos[Math.floor(Math.random() * this.ojos.length)]
            this.boca_actual = []
            this.boca_actual=this.bocas[Math.floor(Math.random() * this.bocas.length)]
            this.orejaI_actual = []
            this.orejaI_actual=this.orejasI[Math.floor(Math.random() * this.orejasI.length)]
            this.orejaD_actual = []
            this.orejaD_actual=this.orejasD[Math.floor(Math.random() * this.orejasD.length)]
            this.nariz_actual = []
            this.nariz_actual=this.narices[Math.floor(Math.random() * this.narices.length)]
            this.accesorio_cabeza = []
            this.accesorio_cabeza=this.accesorios[Math.floor(Math.random() * this.accesorios.length)]

        }
        
    }
})

