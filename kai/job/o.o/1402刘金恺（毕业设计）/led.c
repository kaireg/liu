#include<reg52.h>  	       //库文件
#define uchar unsigned char//宏定义无符号字符型
#define uint unsigned int  //宏定义无符号整型

#define DUAN P0	  //P0口控制段
#define WEI  P2	  //P2口控制位
sbit sz=P1^0;// 更改小时按键
sbit jia=P1^1;// 更改分钟按键
sbit jian=P1^2;// 更改秒按键
sbit LS138A = P2^0;  	//定义138译码器的输入A脚由P2.2控制 
sbit LS138B = P2^1;	    //定义138译码器的输入脚B由P2.3控制
sbit LS138C = P2^2; 	//定义138译码器的输入脚C由P2.4控制
sbit feep=P3^7;
uint f,c=0,v=0,kk=0,hh=0,gg=0;
/********************************************************************
                            初始定义
*********************************************************************/
 uchar Table[11]={0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x40};//七段码对应值
 uint miao=0,fen,shi,smiao,sshi,sfen,dshi=0,dfen=0,yy=0;
void delay(uchar t)
{
  uchar i,j;
   for(i=0;i<t;i++)
   {
   	 for(j=13;j>0;j--);
	 { ;
	 }
   }
}
//************************************************
//延时函数，在12MHz的晶振频率下
//大约50ms的延时
//************************************************
void delay_50ms(uint t)
{
	uint j;
	for(;t>0;t--)
	for(j=6245;j>0;j--);
}
void xians()
{
   
P0=0x00;
LS138A=1; 
LS138B=1; 
LS138C=1;
P0=Table[shi/10];
     delay(80);  

P0=0x00;
LS138A=0; 
LS138B=1; 
LS138C=1;
P0=Table[shi%10];	   
    delay(80);
	   P0=0x00;
LS138A=1; 
LS138B=0; 
LS138C=1;
P0=Table[10];
	 delay(80);
	   P0=0x00;
LS138A=0; 
LS138B=0; 
LS138C=1;
P0=Table[fen/10];
    delay(80);
	   P0=0x00;
LS138A=1; 
LS138B=1; 
LS138C=0;
P0=Table[fen%10];
	 delay(80);
	   P0=0x00;
LS138A=0; 
LS138B=1; 
LS138C=0;
P0=Table[10];
	 delay(80);
	   P0=0x00;
LS138A=1; 
LS138B=0; 
LS138C=0;
P0=Table[miao/10];
	  delay(80);
	   P0=0x00;
LS138A=0; 
LS138B=0; 
LS138C=0;
P0=Table[miao%10];
	   delay(80);
}
//设置时间
void shez()
{
c++;
P0=0x00;
LS138A=1; 
LS138B=1; 
LS138C=1;
if(hh==1)
{
if(c<=25)
{
  P0=Table[sshi/10];
}
else if(c>25&&c<=50)
{
   P0=0x00;
}
else  if(c>50)
{
   c=0;
}
}
else if(hh==2||hh==3||hh==4)
{
    P0=Table[sshi/10];
}
//P0=Table[sshi/10];
 delay(80);  
P0=0x00;
LS138A=0; 
LS138B=1; 
LS138C=1;
if(hh==2)
{
if(c<=25)
{
 P0=Table[sshi%10];	
}
else if(c>25&&c<=50)
{
    P0=0x00;
}
else if(c>50)
{
c=0;
}
}
else if(hh==1||hh==3||hh==4)
{
  P0=Table[sshi%10];	 
}   
 delay(80);  
	   P0=0x00;
LS138A=1; 
LS138B=0; 
LS138C=1;
P0=Table[10];
 delay(80);  
	   P0=0x00;
LS138A=0; 
LS138B=0; 
LS138C=1;
if(hh==3)
{
if(c<=25)
{
P0=Table[sfen/10];
}
else if(c>25&&c<=50)
{
    P0=0x00;
}
else if(c>50)
{
c=0;
}
}
else if(hh==1||hh==2||hh==4)
{
  P0=Table[sfen/10];	 
} 
 delay(80);  
	   P0=0x00;
LS138A=1; 
LS138B=1; 
LS138C=0;
if(hh==4)
{
if(c<=25)
{
P0=Table[sfen%10];
}
else if(c>25&&c<=50)
{
    P0=0x00;
}
else if(c>50)
{
c=0;
}
}
else if(hh==1||hh==2||hh==3)
{
 P0=Table[sfen%10]; 	 
} 
 delay(80);  
	   P0=0x00;
LS138A=0; 
LS138B=1; 
LS138C=0;
P0=Table[10];
 delay(80);  
	   P0=0x00;
LS138A=1; 
LS138B=0; 
LS138C=0;
P0=Table[smiao/10];
 delay(80);  
	   P0=0x00;
LS138A=0; 
LS138B=0; 
LS138C=0;
P0=Table[smiao%10];
 delay(80);  	 
}
//定时时间
void dings()
{
v++;
P0=0x00;
LS138A=1; 
LS138B=1; 
LS138C=1;
if(hh==5)
{
if(v<=25)
{
  P0=Table[dshi/10];
}
else if(v>25&&v<=50)
{
   P0=0x00;
}
else  if(v>50)
{
   v=0;
}
}
else if(hh==6||hh==7||hh==8)
{
    P0=Table[dshi/10];
}
//P0=Table[sshi/10];
 delay(80);  
P0=0x00;
LS138A=0; 
LS138B=1; 
LS138C=1;
if(hh==6)
{
if(v<=25)
{
 P0=Table[dshi%10];	
}
else if(v>25&&v<=50)
{
    P0=0x00;
}
else if(v>50)
{
v=0;
}
}
else if(hh==5||hh==7||hh==8)
{
  P0=Table[dshi%10];	 
}   
 delay(80);  
	   P0=0x00;
LS138A=1; 
LS138B=0; 
LS138C=1;
P0=Table[10];
 delay(80);  
	   P0=0x00;
LS138A=0; 
LS138B=0; 
LS138C=1;
if(hh==7)
{
if(v<=25)
{
P0=Table[dfen/10];
}
else if(v>25&&v<=50)
{
    P0=0x00;
}
else if(v>50)
{
v=0;
}
}
else if(hh==5||hh==6||hh==8)
{
  P0=Table[dfen/10];	 
} 
 delay(80);  
	   P0=0x00;
LS138A=1; 
LS138B=1; 
LS138C=0;
if(hh==8)
{
if(v<=25)
{
P0=Table[dfen%10];
}
else if(v>25&&v<=50)
{
    P0=0x00;
}
else if(v>50)
{
v=0;
}
}
else if(hh==5||hh==6||hh==7)
{
 P0=Table[dfen%10]; 	 
} 
 delay(80);  
	   P0=0x00;
LS138A=0; 
LS138B=1; 
LS138C=0;
P0=Table[10];
 delay(80);  
	   P0=0x00;
LS138A=1; 
LS138B=0; 
LS138C=0;
P0=Table[smiao/10];
 delay(80);  
	   P0=0x00;
LS138A=0; 
LS138B=0; 
LS138C=0;
P0=Table[smiao%10];
 delay(80);  	 
}
/********************************************************************
                           按键函数
*********************************************************************/        

void key()//函数
{
  if(sz==0)
  {
 hh++;
 
 if(hh==1)
 {
 sshi=shi;
 sfen=fen;
 }
 else if(hh>=9)
 {
 shi=sshi;
 fen=sfen;
   hh=0;
 }
    while(sz==0);
  }
  if(jia==0)
  {
	 if(sshi<14&&hh==1)
	 {
   	sshi=sshi+10; 	 
	 }
	 else if(hh==2&&sshi<24)
	 {
	 sshi++;
	 }
	 else if(hh==3&&sfen<50)
	 {
	 sfen=sfen+10;
	 }
	 else if(hh==4&&sfen<60)
	 {
	 sfen++;
	 }
	 else	 if(dshi<14&&hh==5)
	 {
   	dshi=dshi+10; 	 
	 }
	 else if(hh==6&&dshi<24)
	 {
	 dshi++;
	 }
	 else if(hh==7&&dfen<50)
	 {
	 dfen=dfen+10;
	 }
	 else if(hh==8&&dfen<60)
	 {
	 dfen++;
	 }
	 while(jia==0);
  }
    if(jian==0)
  {
	 if(sshi>10&&hh==1)
	 {
   	sshi=sshi-10; 	 
	 }
	 else if(hh==2&&sshi>0)
	 {
	 sshi--;
	 }
	 else if(hh==3&&sfen>10)
	 {
	 sfen=sfen-10;
	 }
	 else if(hh==4&&sfen>0)
	 {
	 sfen--;
	 }
	 else	 if(dshi>10&&hh==5)
	 {
   	dshi=dshi-10; 	 
	 }
	 else if(hh==6&&dshi>0)
	 {
	dshi--;
	 }
	 else if(hh==7&&dfen>10)
	 {
	 dfen=dfen-10;
	 }
	 else if(hh==8&&dfen>0)
	 {
	 dfen--;
	 }
	 while(jian==0);
  }
}



/********************************************************************
                           中断初始化
*********************************************************************/

void cshh()
{ 
 TMOD=0X01;//定义定时器工作方式
	TH0=(65536-50000)/256; //设置初值	// 50000
	TL0=(65536-50000)%256;
	EA=1;      //打开总中断开关
	ET0=1;     //打开定时器中断
	TR0=1;	   //关闭定时器0
 }
 
/********************************************************************
                            主函数
*********************************************************************/

main()
{
feep=0;
cshh();	 //中断初始化

while(1)
{
 key();//按键函数
 if(hh==0)
 {
 xians();
 }
 else if(hh==1||hh==2||hh==3||hh==4)
 {
  shez();
 }
 else if(hh==5||hh==6||hh==7||hh==8)
 {
   dings();
 }
  if(dshi==shi&&dfen==fen&&yy==1)
  {
  feep=1;
 delay_50ms(10);
  feep=0;
    delay_50ms(10);
	  feep=1;
     delay_50ms(10);
	   feep=0;
  delay_50ms(10);
	  feep=1;
     delay_50ms(10);
	   feep=0;
	   
  }
	if(gg==1)
	{
			   feep=1;
			   delay_50ms(20);
			   feep=0;
			   gg=0;	
	}
}
}
/********************************************************************
                           定时器中断函数
*********************************************************************/

void timer0 () interrupt 1
{ 

	TH0=(65536-50000)/256; //设置初值
	TL0=(65536-50000)%256;
  kk++;
 if(kk>=20)
   {
   kk=0;
    miao++;//秒加1
     if(miao>=60)
       {miao=0;//秒清零
	     fen++;//60秒后分加1
		yy=1;
	       if(fen>=60)
	        {fen=0;//分清零
	           shi++;//60分后时加1
				gg=1;
	             if(shi>=24)
				 {
	                   shi=0;//时清零				 
				 }

					          }
	                           }
							   
                                  
}
}
/********************************************************************
                              结束
*********************************************************************/


