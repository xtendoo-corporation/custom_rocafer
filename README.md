**Guia de uso Rocafer en Odoo.**

### **Crear un cliente.**

Para crear un cliente vamos al módulo de Contactos.  
![image14](https://github.com/user-attachments/assets/39f3b60d-d6f0-49f9-aacb-293d856143e4)

Cuando creemos un contacto al que vamos a realizar una venta/fabricacion debemos seleccionar que el contacto sea del tipo “Compañía”
![image8](https://github.com/user-attachments/assets/2c77c062-c639-4125-aa6f-f18d04ded5f5)

### 

### **Crear un producto.**

Para crear un producto vamos al módulo de inventario.  
![image42](https://github.com/user-attachments/assets/c7ab399a-3d33-4ce0-9f40-0a86fb2fe975)

En la barra superior encontraremos varias opciones, desde el apartado configuración nos aparecerá una serie de opciones clasificadas por una cabecera. Donde hay un apartado especial de Rocafer que es donde vamos a personalizar nuestros campos.  
![image37](https://github.com/user-attachments/assets/5a87e02a-1780-4a7c-ada9-43bfe9eeabe1)

La configuración Colores/Estampaciones/Materiales/Barnices son idénticas vamos a tomar como ejemplo la configuración de colores.

Seleccionamos “Color” y nos aparecerá un listado de colores registrados.  
![image24](https://github.com/user-attachments/assets/359dce1f-2163-4983-bb48-e570681625a6)

#### **Añadir un elemento**

Podemos añadir más colores seleccionando “+Nuevo”  
![image18](https://github.com/user-attachments/assets/da69f1a9-9bad-484e-85b3-b02d711af522)

El nuevo color registrado aparecerá en la lista.  
![image20](https://github.com/user-attachments/assets/dc3c342c-9039-4375-84be-d45d3ec26f56)

#### 

#### **Editar un elemento**

Para ello seleccionamos un elemento simplemente haciendo click en él. Editamos su nombre y pulsamos sobre la nube que aparece para guardar los cambios.  
![image28](https://github.com/user-attachments/assets/5bd105fb-84f5-4cb5-925e-e912ccab6b0b)

#### **Eliminar un elemento**

Seleccionamos el check que se encuentra junto a su nombre, pulsamos sobre “Acciones” y seleccionamos la opción eliminar.
![image33](https://github.com/user-attachments/assets/6d3ba9da-ed57-4a4f-a00f-17dcab6d9604)

#### 

#### **Orientaciones**

Las orientaciones de las etiquetas se han creado según el siguiente listado:  
![image19](https://github.com/user-attachments/assets/3d334094-f961-4f3b-b317-9a7aa1d6f38f)

Podemos crear nuevas orientaciones seleccionando “+Nuevo”, o bien podemos editar cualquiera de ellas seleccionando una orientación de la lista.  
![image1](https://github.com/user-attachments/assets/36eccf89-977a-45c2-bc55-45506e403256)

Seleccionando una orientación podemos editar tanto su denominación como su imagen.  
![image6](https://github.com/user-attachments/assets/fe9594c8-5403-49ca-8440-47b778e621f0)

#### **Cilindros de impresión**

Los cilindros de impresión se han registrado según el excel que contiene esta información.  
![image9](https://github.com/user-attachments/assets/366d1b61-2683-45ec-88af-425576e23ba2)

Para editar o visualizar el contenido de “Omet 58/116” pulsamos sobre el.  
![image3](https://github.com/user-attachments/assets/0ae47fa7-0af4-44e0-a616-8cac6513efab)

Desde esta vista podemos editar, agregar o eliminar los valores del tamaño del cilindro.  
![image30](https://github.com/user-attachments/assets/96419de2-ff78-4dfb-948f-2cca0b3bdac5)

#### **Crear un producto**

Desde la barra superior de inventario, seleccionamos “Productos”  
![image16](https://github.com/user-attachments/assets/3f2d43f7-e985-4d4b-bdd2-cd0cb24dd6c8)

Obtendremos la lista de productos creados.  
![image11](https://github.com/user-attachments/assets/941de0f6-8c7a-4a49-9f63-0441859068e0)

Vamos a crear el producto “Etiqueta bote proteinas” para ello desde la lista de productos pulsamos en “+Nuevo”, es **importantísimo** que esté marcado “Puede ser vendido” para que Odoo pueda listar el producto en un presupuesto o venta. Esta opción viene marcada por defecto al crear un producto.  
![image29](https://github.com/user-attachments/assets/b04a8888-5f59-45d2-a146-fe0731dcf65d)

En la pestaña Inventario debe estar marcado “**Obtener Bajo Pedido (MTO)**” y “**Fabricar**”, la opción de “**Comprar**” **hay que desmarcarla** para generar una fabricación al realizarse una venta. Desde Xtendoo hemos definido por defecto que estos campos aparecen por defecto.
![2024-08-12_10-24](https://github.com/user-attachments/assets/f61305de-ca7f-435a-9264-a2aeb808f7d6)

En la pestaña Datos Rocafer es donde vamos a aportar toda la información sobre la fabricación de esta etiqueta.

El apartado **CLIENTE** se seleccionará entre todos los clientes registrados en Odoo al que le vamos a realizar la fabricación/venta.
![image4](https://github.com/user-attachments/assets/7174dee7-a056-426d-8999-8476b5402be8)

El apartado **TROQUEL 1** contiene información del troquel sobre el que se realizarán los cálculos.  
![image23](https://github.com/user-attachments/assets/7aa6e32c-b4ef-46ad-a426-c53470d5b798)

El apartado **TROQUEL 2** contiene información de otro troquel, sobre este este troquel NO se realizan cálculos.
![image36](https://github.com/user-attachments/assets/183f2051-2a38-4a81-9988-ab37b63d237f)

El apartado **PRODUCCIÓN** según se vayan introduciendo los campos se calcularán conforme al cilindro de impresión calculado.  
![image26](https://github.com/user-attachments/assets/34eeb62c-c2d7-46c0-a259-8290bba41d85)

El apartado **CILINDRO DE IMPRESIÓN** muestra el cilindro de impresión más coincidente con los datos introducidos y con el que se realizan los cálculos del apartado de producción.  
![image25](https://github.com/user-attachments/assets/314539b9-0ad6-4728-9753-b6d0206f1c9d)

El apartado **MATERIALES** contiene información sobre la etiqueta.  
![image12](https://github.com/user-attachments/assets/4c76251c-c881-46f2-92f8-44f58937e2d3)

En el apartado **ORIENTACIÓN** podemos elegir una orientación entre las registradas.  
![image38](https://github.com/user-attachments/assets/81914fa3-1a8c-470f-91bc-82b4c2a22827)

Al final de la página se pueden registrar comentarios para diversas áreas.
![image15](https://github.com/user-attachments/assets/ea621304-4ed9-4396-bf97-47c81ea9eccc)

Una vez terminado guardamos pulsando sobre la nube.  
![image2](https://github.com/user-attachments/assets/18bf5129-019d-412c-a637-cf301cb8555a)

#### **Instrucciones de Fabricación**

En la parte superior hay un botón para crear una lista de materiales para la fabricación del producto
![image36](https://github.com/user-attachments/assets/aeb70a46-6c14-4c3c-87fc-7d34951e605c)

![image4](https://github.com/user-attachments/assets/0a124e06-85d0-45e9-a6e3-e7a2f57157d5)

En lista de materiales podemos establecer los componentes y las operaciones que necesitamos para la fabricación del producto, en nuestro caso iremos a operaciones y agregaremos las operaciones que necesite la fabricación del producto como puede ser Fabricación y Revisión.
![image24](https://github.com/user-attachments/assets/b81afea0-5443-4f5a-9b77-f3c8ef32b483)

A la hora de crear una fabricación deberiamos de seleccionar "Calcular según el tiempo registrado" para que se haga una estimación del tiempo de fabricación segun las ultimas 10 fabricaciones. 
![2024-09-25_11-46](https://github.com/user-attachments/assets/2a265219-ac02-4495-a693-937e049e0543)

### **Realizar una venta del producto.**

Para crear una venta o presupuesto vamos al módulo de Ventas.  
![image7](https://github.com/user-attachments/assets/91f61eb4-bf6a-4fe8-a434-d737e141ad0b)

Realizamos un presupuesto pulsando sobre “+Nuevo”  
![image40](https://github.com/user-attachments/assets/4d2cc412-d246-4778-9a8d-489feff28820)

Seleccionamos el cliente y en “Líneas de pedido” solo podremos elegir los productos relacionados con el cliente que seleccionamos en el apartado del producto.  
![image21](https://github.com/user-attachments/assets/174f96d3-2ec7-45ac-99e5-2632feff343f)

Una vez establecida la cantidad y el precio, vamos a la pestaña “Otra información” donde añadiremos la Referencia cliente y la Fecha de entrega.  
![image39](https://github.com/user-attachments/assets/99df3e61-18b9-43e7-85ef-49b3d00433e0)
![image17](https://github.com/user-attachments/assets/806a80ae-717f-4e58-beb0-f8ea6944c283)

Confirmamos el presupuesto y este recibirá un número de presupuesto.

![image27](https://github.com/user-attachments/assets/c7695577-6ce8-4077-b719-b480cce33311)

#### **Imprimir la orden de trabajo**

Una vez que tengamos un presupuesto enumerado podemos imprimir la orden de trabajo desde el engranaje.  
![image35](https://github.com/user-attachments/assets/49cc9d7e-8d92-42ab-a3b8-24df6ae129f7)

Resultado de la impresión.  
![image31](https://github.com/user-attachments/assets/41313ff6-2b41-410e-8567-b3da8160ee2d)

En el presupuesto aparecerá una llave con la Fabricación  
![image34](https://github.com/user-attachments/assets/ea167c98-5913-4a2c-8aa6-9500534ae945)

Por defecto en nuestra orden de fabricación aparecerá Fabricación y Revisión. Aquí debemos añadir editar o eliminar tantas operaciones como quiera.

El empleado se debe asignar y el centro de trabajo está por defecto la Línea 1 con posibilidad de cambiarlo en cualquier momento.   
![image13](https://github.com/user-attachments/assets/a911c38d-b62f-4e07-b83f-f33a43ac8038)

Para tener una vista general de las fabricaciones vamos al módulo de Fabricación  
![image5](https://github.com/user-attachments/assets/2c7d02b0-07ea-40da-9436-e965fce06102)

Seleccionamos Órdenes de trabajo  
![image22](https://github.com/user-attachments/assets/a1ffb08b-342d-45bf-b37e-88e92518b938)

Se mostrarán las órdenes de trabajo que aún no estén finalizadas, para visualizarlas por centros de trabajo, pulsamos sobre el desplegable que hay en el buscador y marcamos “Centro de trabajo”  
![image32](https://github.com/user-attachments/assets/65194a9f-4f7f-4fa3-92dd-a2310ecca1f9)

Esto mostrará las órdenes de trabajo agrupadas por los centros de trabajo y toda la información de la venta.  
![image41](https://github.com/user-attachments/assets/9eb6a87f-4f37-4083-84ee-0719549c20f0)

Una vez finalizada la orden de trabajo daremos por finalizada la fabricación pulsando sobre el botón “Producir todo”  
![image2](https://github.com/user-attachments/assets/83129c3b-dade-4b68-8c41-abf93719c787)

Es posible que salte una advertencia de confirmación, no es relevante en nuestro caso de uso ya que nuestros productos no se forman a partir de otros componentes.  
![image1](https://github.com/user-attachments/assets/7930ab7d-8320-4aca-88af-fa1cc12a21cb)

### **Entregas**

Volvemos a la venta de nuestro producto y ahora si pulsamos en “Entrega” obtendremos información relevante sobre nuestra venta.  
![image3](https://github.com/user-attachments/assets/194ab99e-bc7f-4175-8e6a-eb6ea74f8623)

Los campos más relevantes son los siguientes, donde la demanda es la cantidad total del pedido y la cantidad es la cantidad que vamos a entregar, de esta forma Odoo nos permite crear entregas parciales.

![image6](https://github.com/user-attachments/assets/1850134b-cb0a-4c47-91e1-404c1b2eb435)

Para imprimir un albarán únicamente debemos pulsar en el botón “Imprimir”, esto creará un albarán donde la entrega aún no ha salido del origen.  
![image7](https://github.com/user-attachments/assets/52222a17-77f7-409a-b7fc-b4526056ff5a)

El estado de nuestros albaranes/entregas se muestra en la parte superior.   
![image13](https://github.com/user-attachments/assets/e6925082-fbf1-4433-83d7-37eb8009937d)

En el momento que pulsemos “Validar” nuestra entrega ya habrá salido del origen.  
![image5](https://github.com/user-attachments/assets/72ff7da7-ea8f-43f6-a1c9-9806390dcffe)

Ahora el estado de nuestra entrega cambia a “Hecho”  
![image9](https://github.com/user-attachments/assets/9a673da3-bb8c-4799-a798-9efcb0c2b10e)

Imprimir albarán  
![image7](https://github.com/user-attachments/assets/85adb86c-0647-4eca-9b88-82b40084bf59)

Imprimir albarán valorado  
![image4](https://github.com/user-attachments/assets/c3d2af8d-ece0-4c2c-94e8-1fb16c432654)

### **Facturación**

En el pedido podemos crear la factura pulsando sobre el botón “Crear Factura”  
![image8](https://github.com/user-attachments/assets/daf0c470-11c6-4be4-a177-395e38884147)

La factura se creará como borrador, es el momento de indicar la fecha de la factura, la referencia el pago, su vencimiento…  
![image11](https://github.com/user-attachments/assets/110acee2-49d4-41f1-9525-b93bfd8a8144)

A qué cuenta contable irá cada línea de producto  
![image12](https://github.com/user-attachments/assets/4bca49a0-e3b2-4004-9afa-08bdd148e08d)

Una vez rellenados estos datos confirmaremos nuestro borrador y podemos enviar la factura al cliente, registrar su pago…  
![image10](https://github.com/user-attachments/assets/604b3056-5510-4a7f-b110-d5ca4e8a94aa)
