using System;

class Program
{
    static void Main()
    {
        var random = new Random();
        int randomNumber = random.Next(1, 101);
        Console.WriteLine($"Rastgele sayı: {randomNumber}");
    }
}
