#include	"unp.h"
#include <stdio.h> 
#include <string.h> 

int
main(int argc, char **argv)
{
	int					sockfd, n;
	char				buff[MAXLINE],in[MAXLINE],out[MAXLINE];
	FILE                *recivedFile;
	struct sockaddr_in	servaddr;

	if (argc != 3)
		err_quit("usage: a.out <IPaddress> <FileName>");

	if ( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
		err_sys("socket error");

	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port   = htons(13);	/* daytime server */
	if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0)
		err_quit("inet_pton error for %s", argv[1]);

	if (connect(sockfd, (SA *) &servaddr, sizeof(servaddr)) < 0)
		err_sys("connect error");
		
	while (in != "bye" ) {
	             if(read(sockfd, in, MAXLINE) > 0);
                    {
                        printf( "%d >>> %s \n",sockfd,in);
                    }
	    }
	if (n < 0)
		err_sys("read error");
	
	fclose(recivedFile);

	exit(0);
}
