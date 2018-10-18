/*
	Restricoes da entrada:
		-Com cabecalho
		-Separado por ", "
*/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class GraphGen
{
	/*
	From a vertex v, finds k generations below it and returns
	a subgraph with a copy of those vertices (and their edges)
	*/
	public static ArrayList<Vertex> getSubgraph(Vertex v, int k)
	{
		//LinkedHashMap keeps the order the elements are added
		//find vertex copies fast
		LinkedHashMap<Vertex, Vertex> vertices = new LinkedHashMap<>();
		ArrayList<Vertex> subgraph = new ArrayList<>();
	
		vertices.put(v, new Vertex(v.getNumber()));
		
		//if there are not any in-going edges the subgraph only has v
		if(v.getInEdges().size() != 0)
		{
			//adds v to subgraph for the start of the recursion
			subgraph.add(v);
			findVerticesRecursive(k, vertices, subgraph);
		}

		subgraph = new ArrayList<>(vertices.values());
		
		return subgraph;
	}

	/*
	recursively analises the vertices in the list to find their in edges. Repeats k times
	makes copies of the vertices and adds them to the list of vertices, links them
	returns a hashmap of the copy of the vertices
	*/
	public static void findVerticesRecursive(int k, LinkedHashMap<Vertex, Vertex> vertices, ArrayList<Vertex> thisGen)
	{
		//nextgen = vertices analyzed on the next recursion
		ArrayList<Vertex> nextGen = new ArrayList<>();
		Vertex newVertex;

		//analyzes each vertex of the list
		for(Vertex v : thisGen)
		{
			//analyzes their edges
			for(Vertex w : v.getInEdges())
			{
				//checks if there is a copy already (to avoid duplicates)
				newVertex = vertices.get(w);

				if(newVertex == null)
				{
					//if there is not a copy, create it and add it to be analyzed next
					//if there is a copy, it was already analyzed
					newVertex = new Vertex(w.getNumber());
					vertices.put(w, newVertex);
					nextGen.add(w);
				}
				
				//adds the edges to the copied vertices
				vertices.get(v).addInEdge(newVertex);
				newVertex.addOutEdge(vertices.get(v));
			}
		}

		//if there is still a generation to consider, continue
		if(k > 1)
			findVerticesRecursive(k-1, vertices, nextGen);
	}

	/*
	based on the second part of the file, links the existing vertices using the
	hashmap to find them
	*/
	public static void linkVertices(Scanner scan, HashMap<Integer, Vertex> map)
	{
		String fields[];

		Vertex v1, v2;

		//while file has lines
		while(scan.hasNext())
		{
			//scan line and split in commas
			fields = scan.nextLine().split(", ");

			//if it is not a number it throws an error
			try
			{
				//v1 = professor
				//v2 = student
				v1 = map.get(Integer.parseInt(fields[0]));
				v2 = map.get(Integer.parseInt(fields[1]));
				
				//invert edge (for inverse PageRank)
				//note: probably should make it regular edges here
				//and invert edges in file
				v2.addOutEdge(v1);
				v1.addInEdge(v2);
			}
			catch(NumberFormatException nfe)
			{
				System.out.println("Error in edge format: "
					+ fields[0]
					+ " and "
					+ fields[1]);
			}
		}
	}

	/*
	creates a new vertex for each line in the file. Uses number in file to number them
	puts in map to link them later
	*/
	public static void createVertices(Scanner scan, HashMap<Integer, Vertex> map, ArrayList<Vertex> graph)
	{
		String fields[];

		fields = scan.nextLine().split(", ");

		try
		{
			for(int i=0; scan.hasNext(); i++)
			{
				graph.add(new Vertex(Integer.parseInt(fields[0])));
				map.put(Integer.parseInt(fields[0]), graph.get(i));

				fields = scan.nextLine().split(", ");
			}
		}
		catch(NumberFormatException nfe)
		{}
	}

	/*
	prepares for the process of building the graph
	creates a scanner for the file, a list for the graph and a map to link them
	*/
	public static ArrayList<Vertex> makeFromFile(String file) throws FileNotFoundException
	{
		Scanner scan = new Scanner(new File(file));

		ArrayList<Vertex> graph = new ArrayList<>();
		HashMap<Integer, Vertex> map = new HashMap<>();

		scan.nextLine(); //removes header

		createVertices(scan, map, graph);

		linkVertices(scan, map);

		return graph;
	}
}