from pathlib import Path
import qrcode


def gerar_qrcode(
    conteudo: str,
    caminho_saida: str = "assets/qrcode.png",
    cor_frente: str = "black", # cores - tem que estar assim vei python tbm tem chatice
    cor_fundo: str = "white",
) -> str:
    if not conteudo.strip():
        raise ValueError("O conteúdo do QR Code não pode estar vazio.") # validando se o conteúdo está vazio

    caminho = Path(caminho_saida)
    caminho.parent.mkdir(parents=True, exist_ok=True) # assusta não, é só caminho de pasta - se não tiver, vai se criar 

    qr = qrcode.QRCode(  #configuração do QR Code
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  #fixo de configuração para 30% de falha 
        box_size=10,  # lembre de css e hmtl
        border=4
    )
    qr.add_data(conteudo) #informação que vai ser codificada no QR Code
    qr.make(fit=True)   #responsividade

    img = qr.make_image(fill_color=cor_frente, back_color=cor_fundo)
    img.save(caminho)

    return str(caminho.resolve())



