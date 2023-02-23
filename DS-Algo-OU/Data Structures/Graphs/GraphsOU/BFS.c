int Stack[5];
int sp = 0;
void push(int data)
{
  if(sp == 5)
  {
    printf("Stack Overflow:\n");
  }
  else
  {
    Stack[sp++] = data;
  }
}

int pop()
{
  if(sp == -1)
  {
    return -1;
  }
  else
  {
    return Stack[--sp];
  }
}
int seek()
{
  if(sp == -1)
  {
    return -1;
  }
  else
  {
    return Stack[sp];
  }
}
int main() {
  int* matrix[5][5] = {{0,0,0,0,1}, {1,0,0,0,0}, {1,0,0,0,0}, {0,0,1,0,0}, {0,0,0,1,0}};
  
  int visited[5] = {1,0,0,0,0};
  push(0);
  
  // traverse through matrix
  for (int i = 0; i < 5; i++)
  {
    for(int j = 0;j < 5; j ++)
    {
      if(
      // if edge exists
      if(matrix[i][j] == 1)
      {
        // if the node is already visited
        if(visited[j] == 1)
        {
          continue;
        }
        else
        {
          push(j);
        }
      }
    }
  }

  return 0;
}
