public class Edge {

    private final Vertex source;

    private final Vertex destination;

    private final String teamandyear;

    private final String hashcode;

    public Edge(Vertex source, Vertex destination,String teamandyear){
        this.source = source;
        this.destination = destination;
        this.teamandyear = teamandyear;

        this.hashcode = source.getname() + destination.getname() + "_" + teamandyear;

    }

    public Vertex getsource(){
        return this.source;

    }

      public Vertex getdestination(){
        return this.destination;
        
    }

      public String getteamandyear(){
        return this.teamandyear;
        
    }

      public String gethashcode(){
        return this.hashcode;
        
    }
    
}
