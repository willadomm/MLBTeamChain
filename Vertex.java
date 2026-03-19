
import java.util.Set;

public class Vertex {
    private final String name;

    private Set<Vertex> teammates;

    public Vertex (String name)
    {
        this.name = name;
    }

    public String getname(){
        return this.name;
    }

    public Set<Vertex> getteammates(){
        return this.teammates;
    }
}
