def remove_duplicates(self):
        if self.head is None or self.head.next is None:
            return None
            
        unique = set()
        runner = self.head
        prev = None
        
        while runner is not None:
            if runner.value in unique:
                next = runner.next
                prev.next = next
                runner = next
            else:
                unique.add(runner.value)
                prev = runner
                runner = runner.next
        
        return self.head