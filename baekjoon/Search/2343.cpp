#include <iostream>
int main() {
    int lesson, blueray_num,blueray[100001];
    scanf("%d %d",&lesson,&blueray_num);
    long long hi = 0;
    for(int i=0;i<lesson;i++){
        scanf("%d",blueray+i);
        hi += blueray[i];
    }
    long long lo = 1;
    
    
    while(lo<hi){
        long long count = 0;
        long long mid = (lo+hi)/2;
        long long pre = mid;
        for(int i=0;i<lesson;i++){
            if(pre>=blueray[i]){
                pre -= blueray[i];
                if(i == lesson-1) count++;
                else if(pre<blueray[i+1]){
                    count++;
                    pre = mid;
                }
            }
            else {
                count = blueray_num+1;
                break;
            }
            
        }
        if(count <= blueray_num) hi = mid;
        else{
            lo = mid;
            if(lo+1 == hi) break;
        }
        
    }
    
    printf("%lld",hi);
    
}