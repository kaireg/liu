#include <reg51.h>
#define uchar unsigned char
#define uint unsigned int
uchar code  table1[]={0x3f,0x006,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x40,0x3f,0x37,0x71};
//数码管位选	         
uchar code table2[]={0x00,0x04,0x02,0x06,0x01,0x05,0x03,0x07};
int umiao,shi,fen,miao,shi1,fen1;
uint k1num,flag;
sbit k1=P1^0;
sbit k2=P1^1;
sbit k3=P1^2;
sbit buzz=P3^7;
/******延时函数******/
void delay(uint t)
{
   uint a;
   for(;t>0;t--)
   	for(a=110;a>0;a--);
}
/*****蜂鸣器函数*****/
void buzzer()
{
	uint b,c;
	for(c=50;c>0;c--)
	{
		buzz=0;
		b=20;
		while(b--);
		buzz=1;
		b=20;
		P0=table1[fen%10];		  
		delay(2);				  
		P0=0x00;				  
	    delay(2);				  
		P2=table2[1];			 
		P0=table1[fen/10];		  
		delay(2);				  
		P0=0x00;				  
	    delay(2);				 
		P2=table2[0];			  
	    P0=table1[miao%10];		  
	    delay(2);				  
		P0=0x00;				  
	    delay(2);				 
	    P2=table2[4];			 
	    P0=table1[miao/10];		  
	    delay(2);				  
		P0=0x00;				  
	    delay(2);				  
	}
	if(k1num==3)
	{
	 	P2=table2[3];			 
	    P0=table1[shi1%10];		  
	    delay(2);				  
		P0=0x00;				  
	    delay(2);				
	    P2=table2[7];			 
	    P0=table1[shi1/10];		 
	    delay(2);				  
		P0=0x00;				  
	    delay(2);				  
	}
	if(k1num==4)
	{
		P2=table2[6];			  
		P0=table1[fen1%10];		  
		delay(2);				  
		P0=0x00;				  
	    delay(2);				 
		P2=table2[1];			  
		P0=table1[fen1/10];		  
		delay(2);				  
		P0=0x00;				  
	    delay(2);				  
	}
	if(k1num==5)
	{
		if(flag!=0)				 
		{						  
		    P2=table2[0];		  
		    P0=table1[12];		  
		    delay(2);			  
			P0=0x00;			  
	        delay(2);			 
		    P2=table2[4];		  
		    P0=table1[11];		  
		    delay(2);			  
			P0=0x00;			  
	        delay(2);			  
		}
		if(flag==0)				 
		{						  
		    P2=table2[0];		  
		    P0=table1[13];		  
		    delay(2);			  
			P0=0x00;			  
	        delay(2);			 
		    P2=table2[4];		  
		    P0=table1[11];		  
		    delay(2);			  
			P0=0x00;			  
	        delay(2);			  
		}
	}
}
/********按键函数********/
void key()
{
	if(k1==0)					  
	{							  
		delay(15);				  
		if(k1==0)				  
		{						 
			k1num++;			  
			while(!k1);			  
			if(k1num==6)		  
			{					  
				k1num=0;		  
			}					  
		}
	}
	if(k1num==1)				  
	{							   
		if(k2==0)				   
		{						  
			delay(15);			   
			if(k2==0)			   
			{					   
				shi++;			   
				while(!k2);		   
				if(shi==24)		   
				{				   
					shi=0;		   
				}				   
			}
		}
		if(k3==0)				  
		{						   
			delay(15);			   
			if(k3==0)			   
			{					  
				shi--;			   
				while(!k3);		   
				if(shi<0)		   
				{				   
					shi=23;		   
				}				   
			}
		}
	}
	if(k1num==2)				   
	{							   
		if(k2==0)				  
		{						  
			delay(15);			  
			if(k2==0)			  
			{					  
				fen++;			  
				miao=0;			  
				while(!k2);		  
				if(fen==60)		  
				{				  
					fen=0;		   
				}				   
			}
		}
		if(k3==0)
		{
			delay(15);
			if(k3==0)
			{
				fen--;
				miao=0;
				while(!k3);
				if(fen<0)
				{
					fen=59;
				}
			}
		}
	}
	if(k1num==3)
	{
		if(k2==0)
		{
			delay(15);
			if(k2==0)
			{
			   shi1++;
			   while(!k2);
			   if(shi1==24)
			   {
			   		shi1=0;
			   }
			}
		}
		if(k3==0)
		{
			delay(15);
			if(k3==0)
			{
			   shi1--;
			   while(!k3);
			   if(shi1<0)
			   {
			   		shi1=23;
			   }
			}
		}
	}
	if(k1num==4)
	{
		if(k2==0)
		{
			delay(15);
			if(k2==0)
			{
			   fen1++;
			   while(!k2);
			   if(fen1==60)
			   {
			   		fen1=0;
			   }
			}
		}
		if(k3==0)
		{
			delay(15);
			if(k3==0)
			{
			   fen1--;
			   while(!k3);
			   if(fen1<0)
			   {
			   		fen1=59;
			   }
			}
		}
	}
	if(k1num==5)
	{
	   if(k2==0)
	   {
	   	  delay(15);
		  if(k2==0)
		  {
		  	 flag=~flag;
			 while(!k2);
		  }
	   }
	}
}
/**shi,fen,miao显示函数**/
void time_display()
{
	P2=table2[0];
    P0=table1[miao%10];
    delay(2);
	P0=0x00;
	delay(2);
    P2=table2[4];
    P0=table1[miao/10];
    delay(2);
	P0=0x00;
	delay(2);

	P2=table2[2];
	P0=table1[10];
	delay(2);
	P0=0x00;
	delay(2);

	P2=table2[6];
	P0=table1[fen%10];
	delay(2);
	P0=0x00;
	delay(2);
	P2=table2[1];
	P0=table1[fen/10];
	delay(2);
	P0=0x00;
	delay(2);

	P2=table2[5];
	P0=table1[10];
	delay(2);
	P0=0x00;
	delay(2);

	P2=table2[3];
    P0=table1[shi%10];
    delay(2);
	P0=0x00;
	delay(2);
    P2=table2[7];
    P0=table1[shi/10];
    delay(2);
	P0=0x00;
	delay(2);
}
/*******主函数*******/
void main()
{
	flag=0;		  //闹钟默认关
	while(1)
	{
		key();
		if(k1num==0)
		{
		   time_display();
		}
	}
}
/****T0的中断函数****/
void int0() interrupt 1
{
	TH0=(65536-50000)/256;
	TL0=(65536-50000)%256;
	umiao++;
	if(umiao==20)
	{
		umiao=0;
		miao++;
		if(miao==60)
		{
			miao=0;
			fen++;
			if(fen==60)
			{
				fen=0;
				shi++;
				buzzer();	
//整点提示，蜂鸣器发音。
				if(shi==24)
				{
					shi=0;
				}
			}	
		}
	}
	//闹钟时间到，蜂鸣器发音一分钟//		  
	if(shi==shi1&fen==fen1&flag!=0&fen<fen1+1)
	{
		buzzer();
	}
}