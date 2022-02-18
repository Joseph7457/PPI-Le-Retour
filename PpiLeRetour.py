Joueur joueur;

void setup()
{size(1000,1000);
joueur = new Joueur(200,0);
}

void draw()
{
background(0);
joueur.run();
}


void keyPressed()
{
  
  if (key == ' ')
  {
  if (joueur != null && joueur.saut)
  {joueur.sauter(-3);
  print("hello");}
  }
  
  if(keyCode == LEFT && (joueur != null) )
  {
  joueur.v[0] = -joueur.vitesse;
  }
  
  if(keyCode == RIGHT && (joueur != null) )
  {
  joueur.v[0] = joueur.vitesse;
  }



}



class Joueur
{

int[]   p    = {500,0};
float[] v    = {10,0};
float[] a    = {0,0};
float   g    = 0.1;
boolean saut = true;
int vitesse  = 10;


Joueur(int x, int y)
{
  p[0] = x;
  p[1] = y;
}

void run()
{
stroke(255);
line(0,800, 1000, 800);
fill(255,125,25);
rectMode(CENTER);
rect(p[0], p[1], 30,30);

println();
printArray(p);
println();
printArray(v);

if (v[0]>0)
{v[0]-=0.1;}

p[0] += v[0];

p[1] += v[1];
v[1] += a[1];
a[1]  = g;

if(p[1]+15 >= 800)
  {p[1] = 800-15;
   v[1] = 0;
   a[1] = 0;
   saut = true;}
else{p[1] += round(v[1]);}
}

void sauter(int vitesse)
{
v[1] = vitesse;
saut = false;
}



}
