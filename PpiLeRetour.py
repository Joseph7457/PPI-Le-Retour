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
