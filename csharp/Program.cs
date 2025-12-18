using System;
using System.Globalization;
using System.Linq;
using System.Windows.Forms;

namespace RandomGenerator;

internal static class Program
{
    [STAThread]
    private static void Main(string[] args)
    {
        if (args.Length > 0 && args[0].Equals("--cli", StringComparison.OrdinalIgnoreCase))
        {
            RunCli(args.Skip(1).ToArray());
            return;
        }

        ApplicationConfiguration.Initialize();
        Application.Run(new RandomForm());
    }

    private static void RunCli(string[] args)
    {
        var seed = (uint)DateTimeOffset.UtcNow.ToUnixTimeSeconds();
        if (args.Length >= 1 && uint.TryParse(args[0], out var parsedSeed))
        {
            seed = parsedSeed;
        }

        if (args.Length == 0 || !int.TryParse(args.Last(), NumberStyles.Integer, CultureInfo.InvariantCulture, out var max))
        {
            Console.Error.WriteLine("Kullanım: dotnet run --cli [tohum] <üst_sınır>");
            Environment.Exit(1);
            return;
        }

        var rng = new LcgRandom(seed);
        try
        {
            var value = rng.NextInt(max);
            Console.WriteLine(value);
        }
        catch (ArgumentOutOfRangeException ex)
        {
            Console.Error.WriteLine(ex.Message);
            Environment.Exit(1);
        }
    }
}
