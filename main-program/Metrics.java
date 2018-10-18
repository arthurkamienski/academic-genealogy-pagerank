import java.util.ArrayList;
import java.util.HashSet;

public class Metrics
{
	public static ArrayList<ArrayList<Vertex>> generations(ArrayList<Vertex> graph)
	{
		ArrayList<ArrayList<Vertex>> generations = new ArrayList<>();
		HashSet<Vertex> added = new HashSet<>();

		generations.add(new ArrayList<>());

		for(Vertex v : graph)
			if(v.getOutEdges().size() == 0)
			{
				generations.get(0).add(v);
				added.add(v);
			}

		findGenerations(generations, added, 0);

		return generations;
	}

	public static void findGenerations(ArrayList<ArrayList<Vertex>> generations, HashSet<Vertex> added, int number)
	{
		generations.add(new ArrayList<>());
		
		ArrayList<Vertex> thisGen = generations.get(number);
		ArrayList<Vertex> nextGen = generations.get(number+1);

		for(Vertex v : thisGen)
			for(Vertex w : v.getInEdges())
				if(!added.contains(w))
				{
					added.add(w);
					nextGen.add(w);
				}

		if(!nextGen.isEmpty())
			findGenerations(generations, added, number+1);
	}
}