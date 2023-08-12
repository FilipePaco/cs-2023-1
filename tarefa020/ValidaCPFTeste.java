
import static org.testng.Assert.*;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

public class ValidaCPFTeste {

    public void testCPFValido() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfValido = "12345678909";
        boolean resultado = validaCPF.isCPF(cpfValido);
        Assert.assertTrue(resultado);
    }

    @Test
    public void testCPFFormatadoValido() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfValido = "123.456.789-09";
        boolean resultado = validaCPF.isCPF(cpfValido);
        Assert.assertTrue(resultado);
    }

    @Test
    public void testCPFComDigitoVerificadorInvalido() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "12345678901"; // Digito verificador deveria ser 09
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFMenosDe11Digitos() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "123";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFMaisDe11Digitos() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "1234567890987";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComCaracteresNaoNumericos() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "123456a8909";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComTodosOsNumerosIguais() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "00000000000";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComPrimeiroDigitoVerificadorErrado() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "98765432100"; // Primeiro dígito verificador deveria ser 09
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComSegundoDigitoVerificadorErrado() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "12345678900"; // Segundo dígito verificador deveria ser 09
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComEspacosEmBranco() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "123 456 789 09";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComCaracteresEspeciais() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "123.456.789-09";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComLetrasMaiusculas() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "ABC45678909";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFComLetrasMinusculas() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "abc45678909";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFNulo() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = null;
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFBranco() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = " ";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFTamanhoInvalido() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "123456789";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }

    @Test
    public void testCPFSomenteZeros() {
        ValidaCPF validaCPF = new ValidaCPF();
        String cpfInvalido = "00000000000";
        boolean resultado = validaCPF.isCPF(cpfInvalido);
        Assert.assertFalse(resultado);
    }
}