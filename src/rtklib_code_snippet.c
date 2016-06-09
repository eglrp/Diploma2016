    static void saveoutbuf(rtksvr_t *svr, unsigned char *buff, int n, int index)
    {
        rtksvrlock(svr);

        n=n<svr->buffsize-svr->nsb[index]?n:svr->buffsize-svr->nsb[index];
        memcpy(svr->sbuf[index]+svr->nsb[index],buff,n);
        svr->nsb[index]+=n;

        rtksvrunlock(svr);
    }