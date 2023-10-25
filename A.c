#include <stdio.h>
int main()
{
    int m[20],x,l;
    scanf("%d",&l);
    for(int i=0;i<l;i++)
    {
        scanf("%d",&m[i]);
    }
    
    scanf("%d",&x);
    
    for(int j=0;j<l;j++)
    {
        if(m[j]==x)
        {
            printf("at %d , %d is there",j,x);
            break;
        }
        else if(j==(l-1)) { 
            printf("element not found");
            
        }
    }
}