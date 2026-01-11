public class IntersectionOfTwoLinkedLists{
        class ListNode {
        int val;
        ListNode next;
        ListNode(int x) {
            val = x;
            next = null;
        }
    }
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        // Caso alguma lista seja vazia
        if (headA == null || headB == null) {
            return null;
        }

        // 1. Percorre lista A para contar tamanho e pegar o tail
        ListNode currentA = headA;
        int lengthA = 0;
        ListNode tailA = null;

        while (currentA != null) {
            lengthA++;
            tailA = currentA;
            currentA = currentA.next;
        }

        // 2. Percorre lista B para contar tamanho e pegar o tail
        ListNode currentB = headB;
        int lengthB = 0;
        ListNode tailB = null;

        while (currentB != null) {
            lengthB++;
            tailB = currentB;
            currentB = currentB.next;
        }

        // 3. Se os tails forem diferentes, não há interseção
        if (tailA != tailB) {
            return null;
        }

        // 4. Calcula o delta (diferença de tamanho)
        int delta = Math.abs(lengthA - lengthB);

        // 5. Avança o ponteiro da lista maior
        currentA = headA;
        currentB = headB;

        if (lengthA > lengthB) {
            for (int i = 0; i < delta; i++) {
                currentA = currentA.next;
            }
        } else {
            for (int i = 0; i < delta; i++) {
                currentB = currentB.next;
            }
        }

        // 6. Avança ambos até encontrar o ponto de interseção
        while (currentA != null && currentB != null) {
            if (currentA == currentB) {
                return currentA;
            }
            currentA = currentA.next;
            currentB = currentB.next;
        }

        return null;
    }
}
