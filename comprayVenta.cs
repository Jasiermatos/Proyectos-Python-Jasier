//
Console.WriteLine("TecnoShop");
int numeroproductos;
bool salir=false;

do{
Console.WriteLine("Cuantos productos desea agregar a su inventario inicial?");
numeroproductos=Convert.ToInt32(Console.ReadLine());
}while(numeroproductos<=0);

String[] nombres=new string[numeroproductos];
int[] cantidadstock= new int[numeroproductos];
numeroproductos=cantidadstock.Length;
int[] vendidos= new int[numeroproductos];
int[] comprados= new int[numeroproductos];

for(int i=0; i< nombres.Length;i++)
{
Console.WriteLine($"Ingrese producto {i + 1}:");
nombres[i]=Console.ReadLine()!;
Console.WriteLine($"Ingrese cantidad");
cantidadstock[i]=Convert.ToInt32(Console.ReadLine());
}
while(!salir)
{
Console.WriteLine(@$"
MENU PRINCIPAL
1. vender
2. comprar
3. Salir
");
string decision=Console.ReadLine()!;
switch(decision)
{
case "1":
  venta(nombres, cantidadstock, vendidos, comprados);
break;

 case "2":
  compra(nombres, cantidadstock, vendidos, comprados);
break;

 case "3":
 salir=true;
 for(int i=0; i<nombres.Length;i++)
 {
Console.WriteLine(@$"
productos vendidos: {vendidos}
productos comprados: {comprados}
Productos en stock: {cantidadstock}
");
 }
 break;
}
}
static void venta (String[] nombres, int[] cantidadstock, int[] vendidos, int[] comprados)
{
string respuesta;
do{
Console.WriteLine("Ingrese producto que desee vender: ");
string nombre=Console.ReadLine()!;

int indice= Array.IndexOf(nombres, nombre);
if( indice==-1)
{
    Console.WriteLine("Producto no disponible");
    return;
}
Console.WriteLine("Ingrese la cantidad");
int cantidadV=Convert.ToInt32(Console.ReadLine());
vendidos[indice]+= cantidadV;
cantidadstock[indice]-=cantidadV;

Console.WriteLine("Desea continuar vendiendo? si/no");
respuesta=Console.ReadLine()!.ToLower();
}while(respuesta=="si");
}

/*static void compra (String[] nombres, int[] cantidadstock, int[] vendidos, int[] comprados, ref int numeroproductos)
{
string respuesta;
do{
Console.WriteLine("Ingrese producto que desee comprar: ");
nombres[numeroproductos+1]=Console.ReadLine()!;

/*int indice= Array.IndexOf(nombres, nombre);
if( indice==-1 || indice<=0)
{
    Console.WriteLine("Producto no disponible");
    return;
}
Console.WriteLine("Ingrese la cantidad");
int cantidadC=Convert.ToInt32(Console.ReadLine());
comprados[numeroproductos+1]+= cantidadC;
cantidadstock[numeroproductos+1]+=cantidadC;

Console.WriteLine("Desea continuar comprando? si/no");
respuesta=Console.ReadLine()!.ToLower();
}while(respuesta=="si");
}*/

static void compra(String[] nombres, int[] cantidadstock, int[] vendidos, int[] comprados)
{
string respuesta;
do{
Console.WriteLine("Ingrese producto que desee comprar: ");
string nombre=Console.ReadLine()!;

int indice= Array.IndexOf(nombres, nombre);
if( indice==-1)
{
    Console.WriteLine("Producto invalido");
    return;
}
Console.WriteLine("Ingrese la cantidad");
int cantidadC=Convert.ToInt32(Console.ReadLine());
comprados[indice]+= cantidadC;
cantidadstock[indice]+=cantidadC;

Console.WriteLine("Desea continuar comprando? si/no");
respuesta=Console.ReadLine()!.ToLower();
}while(respuesta=="si");
}