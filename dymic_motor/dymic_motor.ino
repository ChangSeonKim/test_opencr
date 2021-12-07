#include <DynamixelWorkbench.h>
DynamixelWorkbench dxl_wb;

void setup() {
  // put your setup code here, to run once:
  dxl_wb.begin("",1000000);
  dxl_wb.ping(1);
  dxl_wb.ping(2);
  //ping -살아있는 지 죽어있는지 확인
  
  dxl_wb.jointMode(1);
  dxl_wb.jointMode(2);
}

void loop() {
  // put your main code here, to run repeatedly:
  dxl_wb.goalPosition(1,0);
  dxl_wb.goalPosition(2,0);
  delay(2000);
  dxl_wb.goalPosition(1,2000);
  dxl_wb.goalPosition(2,2000);
  delay(2000);
}
