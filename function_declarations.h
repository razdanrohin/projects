#define DISPLAY_MESSAGE 0x34
#define MOTOR_MESSAGE   0x80


/* Define endianness of the data to be processed, since it does not suppport big endian */
#if __BYTE_ORDER != __LITTLE_ENDIAN
   #error(__BIG_ENDIAN is not supported)
#endif


/* packet data structure, compatible for both display function and the motor function */
typedef struct {
   unsigned char   packet_id;
   unsigned char   message_type;
   uint16_t        message_length;
   unsigned char   message_data;
} packet;

/* data structure for the motor message */
typedef struct {
   unsigned char id;
   unsigned char type;
   uint16_t len;
   float forward_back;
   float left_right;
} motor_packet;



