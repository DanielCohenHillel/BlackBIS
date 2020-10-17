#include <stdlib.h>
#include <stdio.h>

// Test linked list
struct Node {
  int data;
  struct Node* next;
};

int add_item(struct Node* head, struct Node* item, int n)
{
  // If inserting at the beginning, switch item with head and point item to head
  if (n==0){
    struct Node temp = *head;
    *head = *item;
    *item = temp;
    head->next = item;
  }
  else{
    // Go to the n-th node and insert the item (point prev to it and it to next)
    struct Node* p = head;
    for (int i=1; i<n; i++){
      p = p->next;
      // If got to the end of the list, return an "error"
      if (p->next == NULL)
        return -1;
    }
    item->next = p->next;
    p->next = item;
  }
  // Success!
  return 0;
}

void print_linked_list(struct Node* head)
{
  int i = 0;
  struct Node* p = head;
  while (p->next != NULL){
    printf("\33[1m\33[35m%d\33[0m ⟶ ", p->data);
    p = p->next;
    i++;
  }
  printf("\33[1m\33[35m%d\33[0m\n", p->data);
}

int main()
{
  // === Initilize list ===
  // head --> second --> third --> NULL
  size_t node_size = sizeof(struct Node);
  struct Node* head   = (struct Node*)malloc(node_size);
  struct Node* first  = (struct Node*)malloc(node_size);
  struct Node* second = (struct Node*)malloc(node_size);
  struct Node* third  = (struct Node*)malloc(node_size);
  
  head->data = 3;
  head->next = second;

  second->data = 4;
  second->next = third;

  third->data = 1;
  third->next = NULL;

  // item to add
  first->data = 1;

  add_item(head, first, 1);

  print_linked_list(head);


  return 0;
}
