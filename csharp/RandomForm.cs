using System;
using System.Globalization;
using System.Windows.Forms;

namespace RandomGenerator;

public class RandomForm : Form
{
    private readonly TextBox _upperBoundBox;
    private readonly Button _generateButton;
    private readonly Label _resultLabel;
    private LcgRandom _rng;

    public RandomForm()
    {
        Text = "LCG Rastgele Sayı";
        Width = 320;
        Height = 200;
        StartPosition = FormStartPosition.CenterScreen;

        var seed = (uint)DateTimeOffset.UtcNow.ToUnixTimeSeconds();
        _rng = new LcgRandom(seed);

        var instruction = new Label
        {
            Text = "Üst sınır (dahil değil):",
            Left = 20,
            Top = 20,
            AutoSize = true
        };

        _upperBoundBox = new TextBox
        {
            Left = 20,
            Top = 45,
            Width = 260
        };

        _generateButton = new Button
        {
            Text = "Üret",
            Left = 20,
            Top = 80,
            Width = 80
        };
        _generateButton.Click += (_, _) => Generate();

        _resultLabel = new Label
        {
            Text = "Sonuç için sınır girin",
            Left = 20,
            Top = 120,
            AutoSize = true
        };

        Controls.AddRange(new Control[] { instruction, _upperBoundBox, _generateButton, _resultLabel });
    }

    private void Generate()
    {
        if (!int.TryParse(_upperBoundBox.Text, NumberStyles.Integer, CultureInfo.InvariantCulture, out var max))
        {
            MessageBox.Show("Lütfen geçerli bir tam sayı girin.", "Hata", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            return;
        }

        try
        {
            var value = _rng.NextInt(max);
            _resultLabel.Text = $"0 ile {max} arasında: {value}";
        }
        catch (ArgumentOutOfRangeException ex)
        {
            MessageBox.Show(ex.Message, "Hata", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
    }
}
