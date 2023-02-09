import os

"""
Stores all the constants throughout the software.
"""

WINDOW_TITLE = 'Beat My Chess AI'
LOGO = 'Images/logo.ico'

ALGORITHM_LIST = ['NegaMax', 'NegaMax & Alpha-Beta', 'NegaScout & Quiesce', 'MTD(f) - Main']
DEPTH_LIST = [2, 3, 4, 5]

# State 1: Pre-Game. GUI elements outside of in-game.
PREGAME_MENU_BAR = [['Menu', ['Start Game', ['Play as White', 'Play as Black'], 'Close Application']],
                    ['Algorithm Info. && Settings', ['Custom Game', ['Select Algorithm', 'Change Search Depth',
                                                     'Algorithm Information'], 'Mode', ['Easy', 'Normal', 'Hard', 'Advanced']]],
                    ['Timer Settings', ['Timer Settings']],
                    ['Help && Info', ['Help && Info']]]
STATE_PREGAME = "Pre-Game - Ready!"

# State 2: In-Game. GUI elements for during gameplay
IN_GAME_MENU_BAR = [['&Menu', ['End Game']],
                    ['Algorithm Information', ['Algorithm Info.']],
                    ['Help && Info', ['Help && Info']]]

STATE_PLAYER_MOVE = "In-Game - Your Move!"
STATE_ENGINE_MOVE = "In-Game - Thinking..."
START_PIECES_NUM = 16

COLOUR_LIST = ['Green', 'Wood']

EXACT_SCORE = 0
LOWER_BOUND_SCORE = 1
UPPER_BOUND_SCORE = 2

# Identifiers for each chess piece
BLANK = 0
PAWN_B = 1
KNIGHT_B = 2
BISHOP_B = 3
ROOK_B = 4
KING_B = 5
QUEEN_B = 6
PAWN_W = 7
KNIGHT_W = 8
BISHOP_W = 9
ROOK_W = 10
KING_W = 11
QUEEN_W = 12

# Layout for chess_board
INIT_BOARD = [[ROOK_B, KNIGHT_B, BISHOP_B, QUEEN_B, KING_B, BISHOP_B, KNIGHT_B, ROOK_B],
              [PAWN_B,] * 8,
              [BLANK, ] * 8,
              [BLANK, ] * 8,
              [BLANK, ] * 8,
              [BLANK, ] * 8,
              [PAWN_W,] * 8,
              [ROOK_W, KNIGHT_W, BISHOP_W, QUEEN_W, KING_W, BISHOP_W, KNIGHT_W, ROOK_W]]

# Import chess piece images
IMG_PATH = 'Images'  # Path to images
IMG_BLANK = os.path.join(IMG_PATH, 'blank.png')
IMG_PAWN_B = os.path.join(IMG_PATH, 'b_pawn.png')
IMG_PAWN_W = os.path.join(IMG_PATH, 'w_pawn.png')
IMG_ROOK_B = os.path.join(IMG_PATH, 'b_rook.png')
IMG_ROOK_W = os.path.join(IMG_PATH, 'w_rook.png')
IMG_KNIGHT_B = os.path.join(IMG_PATH, 'b_knight.png')
IMG_KNIGHT_W = os.path.join(IMG_PATH, 'w_knight.png')
IMG_BISHOP_B = os.path.join(IMG_PATH, 'b_bishop.png')
IMG_BISHOP_W = os.path.join(IMG_PATH, 'w_bishop.png')
IMG_QUEEN_B = os.path.join(IMG_PATH, 'b_queen.png')
IMG_QUEEN_W = os.path.join(IMG_PATH, 'w_queen.png')
IMG_KING_B = os.path.join(IMG_PATH, 'b_king.png')
IMG_KING_W = os.path.join(IMG_PATH, 'w_king.png')

PIECE_IMAGES = {BISHOP_B: IMG_BISHOP_B, BISHOP_W: IMG_BISHOP_W, PAWN_B: IMG_PAWN_B, PAWN_W: IMG_PAWN_W,
                KNIGHT_B: IMG_KNIGHT_B, KNIGHT_W: IMG_KNIGHT_W, ROOK_B: IMG_ROOK_B, ROOK_W: IMG_ROOK_W,
                KING_B: IMG_KING_B, KING_W: IMG_KING_W, QUEEN_B: IMG_QUEEN_B, QUEEN_W: IMG_QUEEN_W, BLANK: IMG_BLANK}

CLICKED_LIGHT_COLOUR = '#00A35A'                # Colour if light square clicked
CLICKED_DARK_COLOUR = '#008148'                 # Colour if dark square clicked

"""game Constants"""
HIGHLIGHT_LIGHT = '#80DED9'                     # Colour to highlight potential moves - light sq
HIGHLIGHT_DARK = '#3CCDC6'                      # Colour to highlight potential moves - dark sq
STARTER_PGN = {'Event': 'Player vs Engine',   # Starting PGN tags
               'White': 'Player',
               'Black': 'Engine'}

"""evaluator Constants"""
PAWN_SCORE = 100                # Piece value a pawn
MAX_SCORE = PAWN_SCORE * 100    # Maximum score awarded in static evaluation
"""Value of each piece: (old vals shown to side)"""
PIECE_VALUE = [100,             # PAWN:   100
               300,             # KNIGHT: 400
               330,             # BISHOP: 410
               600,             # ROOK: 600
               1000,            # QUEEN: 1200
               9000]               # KING: 0
PHASE_POINTS = [0, 1, 1, 2, 4, 0]

"""Information Windows Text"""
INFO_STR = 'Phần mềm này cung cấp 4 thuật toán tìm kiếm theo mức độ phức tạp tăng dần: ' \
           '\nNegaMax, NegaMax với Alpha-Beta Pruning, NegaScout với thuật tìm kiếm Quiesce và cuối cùng là MTD' \
           '\n\nNegamax: thuật toán cơ bản nhất có thể sử dụng, đây là biến thể khác của thuật toán Minimax. Nó lặp đi lặp lại sơ đồ cây tìm kiếm, ' \
           '\ngọi ra càng hàm tối ưu lần lượt trả lại số điểm cao nhất và thấp nhất. Thuật toán này mô phỏng lại các nước đi tối ưu của người chơi.' \
           '\nThuật toán hoạt động hiệu quả nhất khi thiết lập depth ở mức 2 và 3. Trên mức đó, thuật toán sẽ hoạt động rất chậm và có thể bị làm ' \
           '\nđơ phần mềm. ' \
           '\n\nThuật toán này tương đương mức dễ của phần mềm ' \
           '\n\nThuật toán Negamax với cắt tỉa nhánh alpha-beta: Sự nâng cấp thuật toán Negamax này là nhằm để giảm thiểu độ rộng cây tìm kiếm ' \
           '\nbằng cách loại bỏ sớm các nhánh của sơ đồ cây tìm kiếm bị cho là dư thừa. Thuật toán hoạt động hiệu quả nhất ở detph 3 và càng giảm ' \
           '\nkhả năng về hiệu suất rất nhanh khi càng tăng depth. Vì thế depth được chọn khi sử dụng thuật toán này vẫn nên từ depth 4 trở xuống. ' \
           '\n\nThuật toán này tương đương mức trung bình của phần mềm ' \
           '\n\nThuật toán NegaScout với thuật tìm kiếm Quiescence: Dựa theo thuật toán nêu trên, Negascout giảm thiểu độ rộng cây tìm kiếm ' \
           '\nbằng cách thực hiện nhiều cửa sổ tìm kiếm nhỏ. Một thuật toán nữa là Quiescence, thuật toán ứng dụng chống lại hiệu ứng chân trời ' \
           '\n- horizon effect, bằng cách thực hiện các tìm kiếm ở một nhánh riêng và khác của cây tìm kiếm, nhánh chỉ gồm những quân cờ bị ăn ' \
           '\nhoặc các nước đi chiếu tướng. Tuy tránh được các nước nguy hiểm thuật toán lại kém hiệu quả hơn so với cắt tỉa alpha-beta. Vì thế, ' \
           '\nngười dùng nên để thiết lập depth khi dùng thuật toán này từu 3 trở xuống ' \
           '\n\nThuật toán này cũng tương đương mức khó của phần mềm. Với cải tiến nó sẽ tránh nhiều nước đánh lỗi nguy hiểm hơn ' \
           '\n\nMTD: thuật toán này là chính là phiên bản nâng cấp của thuật toán Negamax với cắt tỉa nhánh alpha-beta, với sự khác biệt là có đặt ra' \
           '\ncác giá trị giới hạn trên và giới hạn dưới được đặt ra để tập hợp các giá trị thực. Đồng thời thuật toán cũng kết hợp cả thuật tìm kiếm ' \
           '\nQuiescence và bảng chuyển vị, kỹ thuật giảm thiểu các phép tính bằng cách ứng dụng cơ chế lưu trữ và thu hồi giá trị và đánh giá bàn cờ. '\
           '\nNhờ tích hợp nhiều thuật toán bổ trợ khác nhau, MTD có thể chạy ở tất cả các depth trong phần mềm. Tuy nhiên, trong một số trường hợp thuật '\
           '\ntoán vẫn gặp vấn đề ở depth 5. Vì thế, để có hiệu quả tốt nhất , hãy thiết lập thuật toán ở depth 4'\
           '\n\nThuật toán này tương đương mức nâng cao của phần mềm ' \

HELP_STR_INIT = 'Chào mừng tới “BeatMyChessAI”, một phần mềm được thiết kế để cho phép bạn thử sức với các ' \
              'thuật toán tìm kiếm mạnh mẽ. Để bắt đầu ván cờ, chỉ cần bấm nút Menu ở trên thanh cửa sổ và tiếp theo ' \
              'là bấm nút Start Game rồi chọn màu phe của bạn. ' \
              '\n\nĐể đổi độ khó của phần mềm, bạn có thể vào phần Mode rồi vào chọn chế độ bạn muốn. ' \
              'Bạn cũng có thể tùy chỉnh kĩ càng độ khó hơn với Custom Game cho phù hợp hơn.' \
              '\n\nBạn có 2 cách để điều chỉnh độ khó cho ván cờ cho vừa với sức mình : ' \
              '\n    Depth: độ sâu của thuật toán càng nông thì càng ít phép tính mà thuật toán cần phải thực hiện,'\
              'từ đó hiệu quả của thuật toán cũng sẽ giảm' \
              '\n    Algorithm: chọn thuật toán sẽ ảnh hưởng mức độ phức tạp của ván cờ. Bạn có thể vào xem chi tiết ' \
              'hướng dẫn chọn các thuật toán ở Algorithm Info' \
              '\n\nBạn cũng có thể tắt bộ đếm giờ để trải nghiệm ván cờ bớt căng thẳng hơn ở Timer Settings.\n'

HELP_STR_INGAME = 'Chào mừng tới “BeatMyChessAI”, một phần mềm được thiết kế để cho phép bạn thử sức với các ' \
              'thuật toán tìm kiếm mạnh mẽ' \
              '\n\nGiờ bạn đang ở trong một ván đánh với một trong các thuật toán!' \
              '\nĐể thực hiện nước đi theo ý mình, đầu tiên bấm vào quân cờ bạn muốn đi và bạn sẽ thấy các nước đi quân cờ đó có thể đi sẽ được đánh dấu màu. ' \
              'Tiếp theo, bấm một trong các ô vuông được đánh dấu màu đó để chọn nước đi.' \
              '\n\nTất cả lịch sử nước đi sẽ được lưu lại để xem. Nó được gọi là Kí pháp Cờ vua ' \
              'từ đó mọi thông tin về ván cờ được giải thích. ' \
              '\n\nKí hiệu của Kí pháp Cờ vua được hiểu như sau như sau :' \
              '\nNước đi: nước đi của mỗi quân cờ sẽ được kí hiệu bởi dạng kí tự kết hợp chữ số như e4, d5,...' \
              '\n\nQuân cờ: quân cờ sẽ được đánh dấu bởi chữ cái đầu đại diện, ví dụ, K = King - Vua, Q = Queen - Hậu' \
              'và R = Rook - Xe. Nếu không có ký tự nào nghĩa là một quân tốt vừa đi' \
              '\n\nCác sự kiện: Có những kí hiệu đại diện cho các nước đi khác nhau trong ván cờ : ' \
              '\nx = Bắt quân, ' \
              '\nO-O/O-O-O = Nhập thành,' \
              '\n+ = Đang chiếu,' \
              '\n# = Chiếu hết.' \
              '' \
              '\n\nNếu bạn muốn kết thúc trò chơi để thay đổi nền, thuật toán hay màu phe, chỉ cần bấm vào menu, ' \
              'bấm kết thúc trò chơi rồi quay trở lại màn hình chờ mà thực hiện các thay đổi.'\
              '\n\nChúc may mắn!\n' \

