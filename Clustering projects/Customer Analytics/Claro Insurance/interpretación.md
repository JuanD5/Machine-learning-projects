# Estamos ante un problema de ventas de autos y motocicletas.

## La tienda es minorista 

## Tenemos cuatro tablas:

### Cliente: todas las características que refieren al cliente

### Producto: precio base y código. 

### Orden: Número de la orden que se relaciona con el ID del cliente, importante el estado de la venta. 

### Detalle de la venta: ID cliente, número de orden de la venta. 

### Todo se puede relacionar con base al ID del cliente. y al número de orden de la venta. 

### Análisis descriptivo:

* Consumo de los clientes: por paises, productos más vendidos, fechas donde suben y bajan las ventas etc. 

* RFM : 
- R de reciente: días transcurridos desde la última compra.
- F de Frecuencia: número de compras realiazadas en un periodo determinado. 
- M de valor monetario: Valor de las compras totales realizadas en un periodo de tiempo. 

#### Esto se hace para cada cliente. (fecha entre 6/01/2003 y 31/05/2005) fecha en formato día mes año. 


#### Tendré que hacer una tabla donde agrupe todo por cliente y poner las 3 columnas correspondientes. 

#### Con base en que puedo segmentar los clientes en clustering?

* Pais
* Total de las ventas
* Cantidad que piden 
* Frecuencia con la que piden 
* La última vez que pidieron 
* Con respecto a la línea de producto como este tipo de cliente pide más de esta línea o esta otra. 


### **Para el sistema de recomendación**:

* Si el cliente compró 3 productos en una orden se le debe recomendar 3 combitos:

El cliente hace una orden

La orden tiene asociada diferentes productos cada producto en diferente cantidad. (la cantidad veo que sería lo único que podría usar como el rating de las peliculas)

Al comprar un producto por x cantidad se le debe ofrecer otro. Lo que no se exactamente es que ofrecer, lo que haría sería poner  el código del producto junto con la línea a la que pertenece y su precio el MSRP. 

Dicen que identifique el producto que más se vendió y proponer 3 combos. Lo que entiendo es:

Cliente : Euroshopping channel 

Número de orden: 10100

Códigos de los productos  que ordenó : 1,2,3,4

Cantidad asociada a cada producto : 10, 30, 40, 15

El producto del cual pidio más es el 3 con 40 unidades. 

A ese producto le debo hacer 3 combos. Como por ejemplo lleve estos  tres productos. 

Pareja (producto 3 , producto recomendado 1 (con sus características)) sería un combito. 

Pareja (producto 3 , producto recomendado 2 (con sus características)) sería otro combito. 

Pareja (producto 3 , producto recomendado 3 (con sus características)) sería otro combito. 

Lo más fácil sería relacionar los productos con respecto a las cantidades que son pedidas. 




      