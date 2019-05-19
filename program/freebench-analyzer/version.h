/* String to identify version */


#ifndef VERSION
#define VERSION "1.00"
#endif

#ifndef COMPDATE
#define COMPDATE "today"
#endif

#ifndef CFLAGS
#define CFLAGS ""
#endif

#ifndef HOSTNAME
#define HOSTNAME "thishost"
#endif

void version()
{
  fprintf(stderr,"--- Dependency Analyzer version: %s, Copyleft 1999 Peter Rundberg ---\n",VERSION);
  fprintf(stderr,"--- Compiled: %s ---\n",COMPDATE);
  fprintf(stderr,"--- Flags: %s ---\n",CFLAGS);
  fprintf(stderr,"--- Host: %s ---\n\n",HOSTNAME);
}
