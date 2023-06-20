# Contador de Objetos usando YOLO

Este é um projeto que utiliza a técnica de detecção de objetos YOLO (You Only Look Once) para contar objetos em tempo real. Ele exibe o vídeo da câmera em uma interface gráfica e identifica objetos em cada frame, mostrando o número total de objetos detectados.

## Funcionalidades

- Detecção de objetos em tempo real usando YOLO
- Contagem do número de objetos detectados
- Interface gráfica para visualização do vídeo e controle da contagem
- Opção para pausar a contagem
- Opção para limpar a tela
- Opção para alterar as cores das caixas delimitadoras e etiquetas
- Opção para usar cores aleatórias nas caixas delimitadoras

## Requisitos

- Python 3.x
- OpenCV
- NumPy
- Tkinter
- Pillow (PIL)

## Como executar

1. Certifique-se de ter todas as bibliotecas mencionadas instaladas.
2. Baixe os arquivos `yolov3.cfg`, `yolov3.weights` e `coco.names` do repositório oficial do YOLO (https://github.com/pjreddie/darknet) e coloque-os na mesma pasta do código.
3. Execute o arquivo `contador_objetos.py` com o Python.

## Uso

1. Ao executar o programa, uma janela será aberta exibindo o vídeo da câmera.
2. Clique no botão "Iniciar Contagem" para começar a contar os objetos.
3. Você verá as caixas delimitadoras e etiquetas sendo desenhadas nos objetos detectados, assim como o número total de objetos na parte inferior da janela.
4. Você pode pausar a contagem clicando no botão "Pausar Contagem".
5. Para limpar a tela, clique no botão "Limpar Tela".
6. Se desejar, você pode alterar as cores das caixas delimitadoras e etiquetas inserindo os valores RGB nas respectivas entradas e clicando no botão "Alterar Cores".
7. Você também pode ativar/desativar cores aleatórias nas caixas delimitadoras marcando ou desmarcando a caixa de seleção "Usar Cores Aleatórias".

## Notas

- Certifique-se de ter uma webcam conectada ou ajuste o código para usar outra fonte de vídeo, se necessário.
- O código foi escrito usando a biblioteca OpenCV para processamento de imagens, Tkinter para a interface gráfica e o modelo YOLO pré-treinado para detecção de objetos.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou correções, sinta-se à vontade para enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
