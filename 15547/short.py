#coding:L1
import zlib
a,b=map(int,input().split());print(' '.join(zlib.decompress('''x�E�]n�0���,��h��^����~\I��w�8	`@�I�|C�om�aG��XSm�6 YǂPK�0tx�D;�+;4�X�Y���u$6y]������棶��D9lc���y����nC7	��[_��)�����zz:մ`or�(DS�i�+>��f�����XF'�Ғ@E�4��f2�g�U���N��%PhA4*eo$y�}{g�˪�h¹Ԕ,�%��%_a�wW�Y��l��g�%;����5����!��؏p������h�2f�̓pG�a<�8��|h;ſg��v�6����A��,>���\rN��\0)�K�x��Kø��+N��W�my�"Ս%�=�QP���?��@'''.encode('L1')).decode().split()[a-1:b]))
